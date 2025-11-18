# Overview 

This app converts text-to-speech. 

This standalone application is designed for local use and is not intended for distribution as a library.

Text-to-speech conversion uses a light-weight neural network running locally. 

The app provides an inbuilt voice. 

The user inputs a local text file and the app converts this text file into an audio output file which plays a faithful narration of the user's text with realistic speech patterns and natural cadence. 

Built in Python and managed with Poetry, this app uses the [neutts-air](https://huggingface.co/neuphonic/neutts-air) model from Hugging Face for speech synthesis. 

For a list of functional requirements and system constraints see the `requirements.md` file.


# Technical Architecture

To ensure separation of concerns, ease of testing, and maintainability, the application employs an Object-Oriented architecture built around a central `Oration` object that orchestrates several specialist service objects.

## User Interface (UI) Module

Responsible for all user interaction. A simple web-based interface handles file uploads, displays status messages, and provides the generated audio for playback. It interacts with an `Oration` object to start the process and monitor its state.

## Oration Class

This class is the core engine of the application, managing the entire lifecycle of a text-to-speech conversion. An instance of this class represents a single job. It will:

*   Receive the input and output file paths.
*   Instantiate a `UserText` and invoke its validation methods.
*   Use a `TextChunker` object to segment the text.
*   Manage the TTS conversion loop, passing chunks to a `Narrator` object.
*   Assemble the final audio file using an `AudioComposition` object.
*   Report its own status and progress back to the UI.

## Core Classes

*   **`Oration`**: Orchestrates the entire validation, chunking, and TTS process for a single run.
*   **`UserText`**: Represents the source text file and contains all validation logic (file size, encoding, word length).
*   **`TextChunker`**: Implements the text-splitting logic based on paragraphs, sentences, or character limits.
*   **`Narrator`**: A wrapper class for the `neutts-air` model, responsible for converting a single text chunk to an audio segment.
*   **`AudioComposition`**: Manages the collection of audio segments and their concatenation into a final `.wav` file.
*   **`exceptions.py`**: Custom exceptions for error handling.

## Application Entry Point

*   **`src/ronda_reade/main.py`**: The main entry point for the application, responsible for launching the UI and initiating the conversion process. To run the app, execute the following command from the project's root directory:
    ```bash
    poetry run ronda-reade
    ```

# Directories
* `/docs`          - Holds all the human-readable documentation.
* `/model`         - Holds the `neuphonic/neutts-air` model files.
