"""
This module contains the AudioComposition class, which handles the
assembly of audio segments into a final audio file.
"""
import numpy as np
import soundfile as sf
from pathlib import Path
from .exceptions import AudioTooLargeError

# Define the maximum size for the audio file in bytes (2 GB)
MAX_AUDIO_SIZE_BYTES = 2 * 1024 * 1024 * 1024

class AudioComposition:
    """
    Manages the collection of audio segments and their concatenation
    into a final audio file, ensuring the total size does not exceed a limit.
    """
    def __init__(self, max_size_bytes: int = MAX_AUDIO_SIZE_BYTES):
        """
        Initializes the AudioComposition.

        Args:
            max_size_bytes: The maximum allowed size for the final audio
                            file in bytes.
        """
        self.max_size_bytes = max_size_bytes
        self.audio_segments: list[np.ndarray] = []
        self.total_size_bytes = 0

    def add_segment(self, segment: np.ndarray):
        """
        Adds an audio segment to the composition after checking size constraints.

        Args:
            segment: A numpy array representing the audio segment.

        Raises:
            AudioTooLargeError: If adding the segment would exceed the max size.
        """
        segment_size = segment.nbytes
        if self.total_size_bytes + segment_size > self.max_size_bytes:
            raise AudioTooLargeError(
                f"Adding this segment would exceed the audio file size limit of "
                f"{self.max_size_bytes / (1024*1024):.0f} MB."
            )
        self.audio_segments.append(segment)
        self.total_size_bytes += segment_size

    def save(self, output_path: Path, samplerate: int = 24000):
        """
        Concatenates the audio segments and saves them to a WAV file.

        Args:
            output_path: The path to save the final audio file.
            samplerate: The sample rate for the output audio file.
        """
        if not self.audio_segments:
            sf.write(output_path, np.array([], dtype=np.float32), samplerate)
            return

        concatenated_audio = np.concatenate(self.audio_segments)
        sf.write(output_path, concatenated_audio, samplerate)
