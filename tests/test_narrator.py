"""Unit tests for the Narrator class."""
import pytest
import numpy as np
from ronda_reade.narrator import Narrator

# Mock the NeuTTSAir model in integration tests (e.g., test_oration.py)
# to avoid slow loading and inference. For this unit test, load the actual
# model to ensure Narrator class instantiation and correct model calls.

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
