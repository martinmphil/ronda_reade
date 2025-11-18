"""Represents the user's input text file and its validation."""
from pathlib import Path
from .exceptions import InvalidTextFileError

class UserText:
    """
    Represents and validates the user's source text file.
    """
    MAX_FILE_SIZE_MB = 5
    MAX_WORD_LENGTH = 50

    def __init__(self, path: Path):
        """
        Initialises the UserText object and validates the associated file.

        Args:
            path: The path to the input text file.
        
        Raises:
            InvalidTextFileError: If the file is invalid.
        """
        self.path = path
        self.content = ""
        self._validate()

    def _validate(self):
        """Performs all validation checks on the text file."""
        file_size_mb = self.path.stat().st_size / (1024 * 1024)
        if file_size_mb > self.MAX_FILE_SIZE_MB:
            raise InvalidTextFileError("This text file is larger than 5 MB.")

        try:
            content = self.path.read_text(encoding='utf-8')
        except UnicodeDecodeError as e:
            raise InvalidTextFileError("Please provide a text file containing only plain text.") from e

        if not content:
            raise InvalidTextFileError("This text file is empty.")

        if any(len(word) > self.MAX_WORD_LENGTH for word in content.split()):
            raise InvalidTextFileError("This file contains overly long words.")
        
        self.content = content
