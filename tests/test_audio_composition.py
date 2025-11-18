"""Unit tests for the AudioComposition class."""
import pytest
import numpy as np
import soundfile as sf
from pathlib import Path
from ronda_reade.audio_composition import AudioComposition

def test_audio_composition_concatenates_and_saves_audio(tmp_path: Path):
    """
    Verify that AudioComposition correctly concatenates audio segments
    and saves them to a WAV file.
    """
    # Create dummy audio segments
    samplerate = 24000
    segment1 = np.zeros(samplerate * 1, dtype=np.float32)  # 1 second of silence
    segment2 = np.ones(int(samplerate * 0.5), dtype=np.float32) * 0.5 # 0.5 seconds of tone
    audio_segments = [segment1, segment2]

    # Instantiate AudioComposition
    composition = AudioComposition(audio_segments)

    # Define output path
    output_file = tmp_path / "output.wav"

    # Save the composition
    composition.save(output_file, samplerate)

    # Assert that the output file exists
    assert output_file.exists()

    # Read the saved file and verify its content
    read_data, read_samplerate = sf.read(output_file)

    # Assert correct samplerate
    assert read_samplerate == samplerate

    # Assert correct total length
    expected_total_length = len(segment1) + len(segment2)
    assert len(read_data) == expected_total_length

    # Assert content (simple check for now)
    assert np.array_equal(read_data[:len(segment1)], segment1)
    assert np.array_equal(read_data[len(segment1):], segment2)
