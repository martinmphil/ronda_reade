"""
This module contains the AudioComposition class, which handles the
assembly of audio segments into a final audio file.
"""
import numpy as np
import soundfile as sf
from pathlib import Path

class AudioComposition:
    """
    Manages the collection of audio segments and their concatenation
    into a final audio file.
    """
    def __init__(self, audio_segments: list[np.ndarray]):
        """
        Initializes the AudioComposition with a list of audio segments.

        Args:
            audio_segments: A list of numpy arrays, each representing an audio segment.
        """
        self.audio_segments = audio_segments

    def save(self, output_path: Path, samplerate: int = 24000):
        """
        Concatenates the audio segments and saves them to a WAV file.

        Args:
            output_path: The path to save the final audio file.
            samplerate: The sample rate for the output audio file.
        """
        if not self.audio_segments:
            # Handle case where there are no segments to concatenate
            # For now, we can create an empty file or raise an error
            # Based on requirements, this scenario should ideally be prevented earlier
            # For now, let's create an empty audio file
            sf.write(output_path, np.array([], dtype=np.float32), samplerate)
            return

        concatenated_audio = np.concatenate(self.audio_segments)
        sf.write(output_path, concatenated_audio, samplerate)
