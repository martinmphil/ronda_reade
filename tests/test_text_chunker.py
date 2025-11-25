"""Unit tests for the TextChunker class."""
from ronda_reade.text_chunker import TextChunker

def test_chunk_by_paragraph():
    """
    Verify that the text is correctly chunked by paragraphs.
    """
    text = "This is the first paragraph.\n\nThis is the second paragraph."
    chunker = TextChunker(text)
    chunks = chunker.chunk()
    assert len(chunks) == 2
    assert chunks[0] == "This is the first paragraph."
    assert chunks[1] == "This is the second paragraph."

def test_chunk_by_sentences_single_paragraph():
    """
    Verify that a single paragraph with more than 5 sentences is chunked.
    """
    # 7 sentences
    text = "Sentence one. Sentence two. Sentence three. Sentence four. Sentence five. Sentence six. Sentence seven."
    chunker = TextChunker(text)
    chunks = chunker.chunk()
    assert len(chunks) == 2
    assert chunks[0] == "Sentence one. Sentence two. Sentence three. Sentence four. Sentence five."
    assert chunks[1] == "Sentence six. Sentence seven."

def test_chunk_by_sentences_multiple_paragraphs():
    """
    Verify that sentence chunking respects paragraph boundaries.
    """
    # Para 1: 3 sentences. Para 2: 3 sentences. Should not be merged.
    text = "P1 S1. P1 S2. P1 S3.\n\nP2 S1. P2 S2. P2 S3."
    chunker = TextChunker(text)
    chunks = chunker.chunk()
    assert len(chunks) == 2
    assert chunks[0] == "P1 S1. P1 S2. P1 S3."
    assert chunks[1] == "P2 S1. P2 S2. P2 S3."

def test_chunk_by_character_limit():
    """
    Verify that a chunk is split when it exceeds the character limit.
    """
    # A single sentence with spaces that is longer than the character limit.
    long_sentence = "word " * 300  # This will be > 1000 chars
    chunker = TextChunker(long_sentence)
    chunks = chunker.chunk()
    assert len(chunks) > 1
    for chunk in chunks:
        assert len(chunk) <= TextChunker.MAX_CHARS




