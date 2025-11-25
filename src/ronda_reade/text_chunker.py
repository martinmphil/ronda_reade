"""This module contains the TextChunker class."""
import nltk
import textwrap

class TextChunker:
    """
    Segments a given text into smaller chunks based on specific rules.
    """
    MAX_SENTENCES = 5
    MAX_CHARS = 1000

    def __init__(self, text: str):
        self.text = text

    def chunk(self) -> list[str]:
        """
        Applies chunking rules to the text.
        """
        # First, split into paragraphs
        paragraphs = [p.strip() for p in self.text.split('\n\n') if p.strip()]

        # Then, split paragraphs into sentence groups
        sentence_chunks = []
        for paragraph in paragraphs:
            sentences = nltk.sent_tokenize(paragraph)
            for i in range(0, len(sentences), self.MAX_SENTENCES):
                sentence_chunk = sentences[i:i + self.MAX_SENTENCES]
                sentence_chunks.append(" ".join(sentence_chunk))

        # Finally, split any oversized chunks by character limit
        final_chunks = []
        for chunk in sentence_chunks:
            if len(chunk) > self.MAX_CHARS:
                # Use textwrap to split the chunk at word boundaries
                wrapped_chunks = textwrap.wrap(
                    chunk, 
                    width=self.MAX_CHARS,
                    break_long_words=False,  # Don't split words
                    break_on_hyphens=False # Don't split on hyphens
                )
                final_chunks.extend(wrapped_chunks)
            else:
                final_chunks.append(chunk)
        
        return final_chunks


