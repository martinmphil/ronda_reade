"""Unit tests for the Narrator class."""
import pytest
import numpy as np
from ronda_reade.narrator import Narrator

# We will mock the NeuTTSAir model to avoid slow model loading and inference
# during unit tests. This will be done in the test_oration.py integration tests.
# For this unit test, we will allow the actual model to load to ensure
# the Narrator class can instantiate and call the model correctly.

def test_narrator_converts_chunk_to_audio():
    """
    Verify that the Narrator class can convert a text chunk into an audio segment.
    """
    # Instantiate the Narrator (this will load the actual TTS model)
    narrator = Narrator()

    # Define a simple text chunk
    text_chunk = "This is a test sentence."

    # Call the method to narrate the chunk
    audio_segment = narrator.narrate_chunk(text_chunk)

    # Assert that an audio segment (numpy array) is returned and it's not empty
    assert isinstance(audio_segment, np.ndarray)
    assert audio_segment.size > 0
