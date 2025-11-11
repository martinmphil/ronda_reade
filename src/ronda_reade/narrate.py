import os
import sys
import warnings

# Suppress the UserWarning from pkg_resources
warnings.filterwarnings("ignore", message="pkg_resources is deprecated as an API")

# Force CPU use by hiding CUDA devices, suppressing PyTorch warnings
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# Define the absolute path to the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add the vendored neutts-air library to the Python path
neutts_air_path = os.path.join(PROJECT_ROOT, 'model', 'neutts-air')
sys.path.append(neutts_air_path)

from neuttsair.neutts import NeuTTSAir
import soundfile as sf

# Initialize the NeuTTSAir model using the local paths
tts = NeuTTSAir(
    backbone_repo="neuphonic/neutts-air-q4-gguf", 
    backbone_device="cpu", 
    codec_repo="neuphonic/neucodec", 
    codec_device="cpu"
)

# Find and read the first .txt file in the input directory
input_dir = os.path.join(PROJECT_ROOT, 'input')
input_text = None
input_filename = None

for filename in sorted(os.listdir(input_dir)):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_dir, filename)
        if os.path.isfile(input_file_path):
            with open(input_file_path, "r", encoding="utf-8") as f:
                input_text = f.read().strip()
            input_filename = filename
            print(f"Using input file: {input_filename}")
            break

if input_text is None:
    print("Error: No .txt file found in the 'input' directory.")
    sys.exit(1)

# Construct portable paths to the reference audio and text files
ref_audio_path = os.path.join(PROJECT_ROOT, 'model', 'neutts-air', 'samples', 'dave.wav')
ref_text_path = os.path.join(PROJECT_ROOT, 'model', 'neutts-air', 'samples', 'dave.txt')

# Read the reference text
with open(ref_text_path, "r") as f:
    ref_text = f.read().strip()

# Encode the reference audio
ref_codes = tts.encode_reference(ref_audio_path)

# Perform inference
wav = tts.infer(input_text, ref_codes, ref_text)

# Save the output audio
output_audio_path = "sound.wav" # This will save in the project root
sf.write(output_audio_path, wav, 24000)

print(f"Audio saved to {output_audio_path}")

# Explicitly clean up the model to prevent shutdown errors
del tts
