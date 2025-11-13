# Overview 

This app converts text-to-speech. 

Text-to-speech conversion uses a light-weight neural network running locally. 

The app provides an inbuilt voice. 

The user inputs a local text file and the app converts this text file into an audio output file which plays a faithful narration of the user's text with realistic speech patterns and natural cadence. 

Built in Python and managed with Poetry, this app uses the [neutts-air](https://huggingface.co/neuphonic/neutts-air) model from Hugging Face for all speech synthesis. 

For a list of functional and non-functional requirements specified in the `requirements.md` file.


# Technical Architecture

To ensure separation of concerns, ease of testing, and maintainability, the application employs a modular, three-part, architecture listed below. 

## User Interface (UI) Module 

Responsible for all user interaction. 

A simple web-based interface handles file uploads, displays status messages, and provides the generated audio for playback. 

## Orchestration Module  

Application logic and core engine. 

The central component of the app, this module will:

  * Receive the input file path from the UI 
  * Invoke a Validation Service 
  * Invoke a Chunking Service 
  * Manage the TTS conversion loop, iterating over text chunks 
  * Enforce rules for time-outs, reties and file size limits 
  * Assemble the final audio file 
  * Report errors and status back to the UI 

## Service Module 

This module is a model-wrapper that manages all direct interaction with the `neutts-air` model machine-learning model. 

This module will: 
    * load the `neutts-air` model from a local directory 
    * generate audio from a given string of text 
    
This module isolates the complex machine-learning code from the rest of the application. 

### AI Model Files 
`neutts-air` manages the downloading and local caching of large AI files (typically in `~/.cache/huggingface/hub`). 

# Files 
* app.py           - Entry point
* ui.py            - Runs the UI application module
* orchestrate.py   - Orchestrates the validation, chunking, and TTS process
* narrator.py      - Wrapper class for the neutts-air model
* validate.py      - Implements all file and text validation rules
* chunking.py      - Implements text-splitting logic
* exceptions.py    - Custom exceptions for error handling

# Directories 
* `/docs`          - Holds all the human-readable documentation. 
* `/model`         - Holds the `neuphonic/neutts-air` model files. 
