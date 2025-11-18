"""
This module contains the Oration class, which orchestrates the
text-to-speech process.
"""
from pathlib import Path
from .user_text import UserText
from .text_chunker import TextChunker
from . import narrator # Changed import

class Oration:
    """
    Orchestrates the entire validation, chunking, and TTS process.
    """
    def __init__(self, input_path: Path):
        self.input_path = input_path
        self.chunks = []
        self.audio_segments = [] # Initialize audio_segments
        self.run()

    def run(self):
        """
        Runs the orchestration process.
        """
        user_text = UserText(self.input_path)
        text_chunker = TextChunker(user_text.content)
        self.chunks = text_chunker.chunk()

        narrator_instance = narrator.Narrator() # Instantiate Narrator
        for chunk in self.chunks:
            audio_segment = narrator_instance.narrate_chunk(chunk)
            self.audio_segments.append(audio_segment)
