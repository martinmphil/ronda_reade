"""Unit tests for the Oration class."""
import pytest
from pathlib import Path
import unittest.mock
import numpy as np
from ronda_reade.oration import Oration

@unittest.mock.patch('ronda_reade.oration.narrator') # Corrected patch target
def test_oration_orchestrates_narrator_correctly(MockNarrator, tmp_path: Path):
    """
    Verify that the Oration class correctly orchestrates the Narrator
    to convert text chunks into audio segments.
    """
    # Setup mock Narrator
    mock_narrator_instance = MockNarrator.Narrator.return_value # Corrected access to mocked class
    dummy_audio_segment = np.array([0.1, 0.2, 0.3], dtype=np.float32)
    mock_narrator_instance.narrate_chunk.return_value = dummy_audio_segment

    # Create a dummy text file with two paragraphs
    test_content = """This is the first paragraph.

This is the second paragraph."""
    test_file = tmp_path / "test.txt"
    test_file.write_text(test_content)

    # Instantiate the orchestrator
    oration = Oration(test_file)

    # Assert that the chunks were created as expected (from previous test)
    assert len(oration.chunks) == 2
    assert oration.chunks[0] == "This is the first paragraph."
    assert oration.chunks[1] == "This is the second paragraph."

    # Assert Narrator was instantiated
    MockNarrator.Narrator.assert_called_once() # Corrected assertion

    # Assert narrate_chunk was called for each chunk
    assert mock_narrator_instance.narrate_chunk.call_count == 2
    mock_narrator_instance.narrate_chunk.assert_any_call("This is the first paragraph.")
    mock_narrator_instance.narrate_chunk.assert_any_call("This is the second paragraph.")

    # Assert audio_segments contains the results
    assert len(oration.audio_segments) == 2
    assert np.array_equal(oration.audio_segments[0], dummy_audio_segment)
    assert np.array_equal(oration.audio_segments[1], dummy_audio_segment)

