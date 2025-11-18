# Ronda Reade

Converting text-to-speech using a local neural network

🖹🡒🗣 

# Summary 
Ronda Reade is a local standalone desktop application for converting text to speech. 

This text-to-speech (TTS) conversion uses the [neutts-air](https://huggingface.co/neuphonic/neutts-air) neural network running locally. The app provides an inbuilt voice. The user inputs a local text file and the app converts this text file into an audio output file which plays a faithful narration of the user's text with realistic speech patterns and natural cadence. 

The Ronda Reade app is not intended for distribution as a library.

# Execution 
```bash
poetry run ronda-reade
```

# Installation
After cloning this repository, run the following terminal command 
```bash
poetry install
```

## System Dependencies 
The 'neutts-air' neural network requires a system installation of `espeak-ng`.
```bash
sudo apt install espeak-ng
```

## Clone Model Source 
Clone the `neutts-air` model code into a directory named `neutts-air` within a `model` directory at the root of this project. 
```bash
git clone https://github.com/neuphonic/neutts-air model/neutts-air
```

# Sources 

## Voice 
[Voice Cloning Toolkit (VCTK) corpus](https://datasets.activeloop.ai/docs/ml/datasets/vctk-dataset/)
