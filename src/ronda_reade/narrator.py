"""
This module contains the Narrator class, which handles text-to-speech conversion
using the NeuTTSAir model.
"""
import os
import sys
import warnings
import numpy as np

# Suppress the UserWarning from pkg_resources
warnings.filterwarnings("ignore", message="pkg_resources is deprecated as an API")

# Force CPU use by hiding CUDA devices, suppressing PyTorch warnings
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# Define the absolute path to the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add the vendored neutts-air library to the Python path
neutts_air_path = os.path.join(PROJECT_ROOT, 'model', 'neutts-air')
sys.path.append(neutts_air_path)

# Import the NeuTTSAir class from the vendored library
from neuttsair.neutts import NeuTTSAir

class Narrator:
    """
    Encapsulates the NeuTTSAir model for text-to-speech conversion.
    """
    def __init__(self):
        """
        Initializes the NeuTTSAir model and loads reference audio.
        """
        self.tts = NeuTTSAir(
            backbone_repo="neuphonic/neutts-air-q4-gguf", 
            backbone_device="cpu", 
            codec_repo="neuphonic/neucodec", 
            codec_device="cpu"
        )

        # Construct portable paths to the reference audio and text files
        ref_audio_path = os.path.join(PROJECT_ROOT, 'voices', 'VCTK_p239', 'VCTK_p239.wav')
        ref_text_path = os.path.join(PROJECT_ROOT, 'voices', 'VCTK_p239', 'VCTK_p239.txt')

        # Read the reference text
        with open(ref_text_path, "r") as f:
            self.ref_text = f.read().strip()

        # Encode the reference audio
        self.ref_codes = self.tts.encode_reference(ref_audio_path)

    def narrate_chunk(self, text_chunk: str) -> np.ndarray:
        """
        Converts a single text chunk into an audio segment.

        Args:
            text_chunk: The text to convert to speech.

        Returns:
            A numpy array representing the audio segment.
        """
        # Perform inference
        wav = self.tts.infer(text_chunk, self.ref_codes, self.ref_text)
        return wav

    def __del__(self):
        """
        Explicitly cleans up the model to prevent shutdown errors.
        """
        if hasattr(self, 'tts'):
            del self.tts