"""Unit tests for the Narrator class."""
import numpy as np
from ronda_reade.narrator import Narrator

def test_narrator_converts_chunk_to_audio():
    """
    Verify that the Narrator class can convert a text chunk into an audio segment.
    """
    # Instantiate Narrator; load actual TTS model.
    narrator = Narrator()

    # Define a simple text chunk.
    text_chunk = "This is a test sentence."

    # Call method to narrate the chunk.
    audio_segment = narrator.narrate_chunk(text_chunk)

    # Assert audio segment (numpy array) is returned and not empty.
    assert isinstance(audio_segment, np.ndarray)
    assert audio_segment.size > 0
