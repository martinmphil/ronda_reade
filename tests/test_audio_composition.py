"""Unit tests for the AudioComposition class."""
import pytest
import numpy as np
import soundfile as sf
from pathlib import Path
from ronda_reade.audio_composition import AudioComposition
from ronda_reade.exceptions import AudioTooLargeError

# Define the maximum size for the audio file in bytes (2 GB)
MAX_AUDIO_SIZE_BYTES = 2 * 1024 * 1024 * 1024

def test_audio_composition_concatenates_and_saves_audio(tmp_path: Path):
    """
    Verify that AudioComposition correctly concatenates audio segments
    and saves them to a WAV file.
    """
    # Create dummy audio segments
    samplerate = 24000
    segment1 = np.zeros(samplerate * 1, dtype=np.float32)  # 1 second of silence
    segment2 = np.ones(int(samplerate * 0.5), dtype=np.float32) * 0.5 # 0.5 seconds of tone
    
    # Instantiate AudioComposition
    composition = AudioComposition()
    composition.add_segment(segment1)
    composition.add_segment(segment2)

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

def test_add_segment_raises_error_if_audio_exceeds_size_limit():
    """
    Verify that adding a segment that exceeds the maximum audio size
    raises an AudioTooLargeError.
    """
    # Instantiate AudioComposition with a smaller, test-specific size limit of
    # 10MB to avoid creating a huge 2GB file in the test.
    test_max_size = 10 * 1024 * 1024  # 10 MB
    composition = AudioComposition(max_size_bytes=test_max_size)

    # Create a segment that is close to the limit
    # An element in a float32 array is 4 bytes.
    # 9MB segment
    segment_size_bytes = 9 * 1024 * 1024
    segment1 = np.zeros(segment_size_bytes // 4, dtype=np.float32)
    composition.add_segment(segment1)

    # Create another segment that will push the total size over the limit
    # 2MB segment
    segment_size_bytes_2 = 2 * 1024 * 1024
    segment2 = np.ones(segment_size_bytes_2 // 4, dtype=np.float32)

    # Assert that adding the second segment raises the correct exception
    with pytest.raises(AudioTooLargeError):
        composition.add_segment(segment2)

    # Verify that the internal state hasn't changed
    assert len(composition.audio_segments) == 1
    assert composition.audio_segments[0].nbytes == segment_size_bytes
    assert composition.total_size_bytes == segment_size_bytes
