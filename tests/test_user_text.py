"""Unit tests for the UserText class."""
import pytest
from pathlib import Path
from ronda_reade.exceptions import InvalidTextFileError
from ronda_reade.user_text import UserText

def test_validate_empty_file_raises_exception(tmp_path: Path):
    """
    Verify that instantiating UserText with an empty file
    raises an InvalidTextFileError.
    """
    # Create an empty file in the temporary directory
    empty_file = tmp_path / "empty.txt"
    empty_file.touch()

    # Assert that the custom exception is raised
    with pytest.raises(InvalidTextFileError, match="This text file is empty."):
        UserText(empty_file)

def test_validate_large_file_raises_exception(tmp_path: Path):
    """
    Verify that instantiating UserText with a file larger than 5MB
    raises an InvalidTextFileError.
    """
    large_file = tmp_path / "large.txt"
    # Create a file that is larger than 5MB
    large_file.write_bytes(b"a" * (5 * 1024 * 1024 + 1))

    with pytest.raises(InvalidTextFileError, match="This text file is larger than 5 MB."):
        UserText(large_file)

def test_validate_encoding_raises_exception(tmp_path: Path):
    """
    Verify that instantiating UserText with a non-UTF-8 encoded file
    raises an InvalidTextFileError.
    """
    non_utf8_file = tmp_path / "non_utf8.txt"
    # Write text using UTF-16 encoding
    non_utf8_file.write_text("test text", encoding="utf-16")

    with pytest.raises(InvalidTextFileError, match="Please provide a text file containing only plain text."):
        UserText(non_utf8_file)

def test_validate_long_word_raises_exception(tmp_path: Path):
    """
    Verify that instantiating UserText with a file containing a word
    longer than 50 characters raises an InvalidTextFileError.
    """
    long_word_file = tmp_path / "long_word.txt"
    long_word = "a" * 51
    long_word_file.write_text(f"This is a normal sentence with a {long_word}.")

    with pytest.raises(InvalidTextFileError, match="This file contains overly long words."):
        UserText(long_word_file)



