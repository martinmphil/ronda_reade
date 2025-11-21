"""
This module contains the Oration class, which orchestrates the
text-to-speech process.
"""
from pathlib import Path
from .user_text import UserText
from .text_chunker import TextChunker
from . import narrator
from . import audio_composition


class Oration:
    """
    Orchestrates the entire validation, chunking, and TTS process.
    """

    def __init__(self, input_path: Path):
        self.input_path = input_path
        self.chunks = []

    def run(self):
        """
        Runs the orchestration process as a generator, yielding progress updates,
        and returns the output file path.
        """
        user_text = UserText(self.input_path)
        text_chunker = TextChunker(user_text.content)
        self.chunks = text_chunker.chunk()
        total_chunks = len(self.chunks)

        narrator_instance = narrator.Narrator()
        audio_composer = audio_composition.AudioComposition()
        
        yield (0.05, "Text processed. Narrating...")

        if total_chunks == 0:
            yield (0.95, "No text to narrate. Assembling audio...")
            output_path = self.input_path.with_suffix(".wav")
            audio_composer.save(output_path, 24000)
            return output_path

        for i, chunk in enumerate(self.chunks):
            audio_segment = narrator_instance.narrate_chunk(chunk)
            audio_composer.add_segment(audio_segment)
            
            narration_progress = (i + 1) / total_chunks
            # Allocate 90% of the bar to narration, starting after initial 5%
            current_total_progress = 0.05 + (narration_progress * 0.90)
            yield (current_total_progress, f"Narrating chunk {i+1} of {total_chunks}")

        yield (0.95, "Assembling audio...")

        output_path = self.input_path.with_suffix(".wav")
        audio_composer.save(output_path, 24000)
        
        return output_path
