"""Custom exceptions for the Ronda Reade application."""

class InvalidTextFileError(ValueError):
    """Exception raised for invalid text files."""
    pass

class AudioTooLargeError(ValueError):
    """Exception raised when the generated audio file exceeds the size limit."""
    pass
