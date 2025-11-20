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

    def run(self, progress=None) -> Path:
        """
        Runs the orchestration process and returns the output file path.
        """
        user_text = UserText(self.input_path)
        text_chunker = TextChunker(user_text.content)
        self.chunks = text_chunker.chunk()

        narrator_instance = narrator.Narrator()
        audio_composer = audio_composition.AudioComposition()
        
        if progress:
            progress(0, desc="Narrating text...")

        chunk_iterator = self.chunks
        if progress:
            chunk_iterator = progress.tqdm(self.chunks, desc="Narrating Chunks")

        for chunk in chunk_iterator:
            audio_segment = narrator_instance.narrate_chunk(chunk)
            audio_composer.add_segment(audio_segment)

        if progress:
            progress(1, desc="Assembling audio...")

        output_path = self.input_path.with_suffix(".wav")
        audio_composer.save(output_path, 24000)
        return output_path
