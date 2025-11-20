"""Unit tests for the Oration class."""
import pytest
from pathlib import Path
import unittest.mock
import numpy as np
from ronda_reade.oration import Oration

@unittest.mock.patch('ronda_reade.oration.audio_composition.AudioComposition')
@unittest.mock.patch('ronda_reade.oration.narrator')
def test_oration_orchestrates_narrator_and_audio_composition_correctly(MockNarrator, MockAudioComposition, tmp_path: Path):
    """
    Verify that the Oration class correctly orchestrates the Narrator
    to convert text chunks into audio segments and then uses AudioComposition
    to save the final audio.
    """
    # Setup mock Narrator
    mock_narrator_instance = MockNarrator.Narrator.return_value
    dummy_audio_segment = np.array([0.1, 0.2, 0.3], dtype=np.float32)
    mock_narrator_instance.narrate_chunk.return_value = dummy_audio_segment

    # Setup mock AudioComposition
    mock_audio_composition_instance = MockAudioComposition.return_value

    # Create a dummy text file with two paragraphs
    test_content = """This is the first paragraph.

This is the second paragraph."""
    test_file = tmp_path / "test.txt"
    test_file.write_text(test_content)

    # Instantiate and run the orchestrator
    oration = Oration(test_file)
    oration.run()

    # Assert Narrator was instantiated
    MockNarrator.Narrator.assert_called_once()

    # Assert narrate_chunk was called for each chunk
    assert mock_narrator_instance.narrate_chunk.call_count == 2
    mock_narrator_instance.narrate_chunk.assert_any_call("This is the first paragraph.")
    mock_narrator_instance.narrate_chunk.assert_any_call("This is the second paragraph.")

    # Assert AudioComposition was instantiated once with no arguments
    MockAudioComposition.assert_called_once_with()

    # Assert add_segment was called for each generated audio segment
    assert mock_audio_composition_instance.add_segment.call_count == 2
    mock_audio_composition_instance.add_segment.assert_called_with(dummy_audio_segment)

    # Assert save method was called with the correct output path and samplerate
    expected_output_path = test_file.with_suffix(".wav")
    mock_audio_composition_instance.save.assert_called_once_with(expected_output_path, 24000)
