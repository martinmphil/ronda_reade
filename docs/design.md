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

The process transforms data as follows: Path ➞ UserText ➞ string ➞ TextChunker ➞ list[str] ➞ Narrator ➞ list[np.ndarray] ➞ AudioComposition ➞ .wav file.

1.  **User Interaction:** The `User` initiates the process by interacting with the `AppUI` (User Interface).
2.  **Orchestration (`Oration`):**
    *   The `AppUI` instantiates and runs the `Oration` object for each text-to-speech conversion job.
    *   `Oration` acts as the central orchestrator, managing the entire lifecycle of the conversion.
3.  **Core Process:**
    *   `Oration` first utilises `UserText` to validate the input text file (e.g., size, format). Any `InvalidTextFileError` is caught and displayed by the `AppUI`.
    *   Next, `Oration` passes the validated text to `TextChunker` to break it into smaller, manageable segments.
    *   `Oration` then iterates through these segments, sending each to the `Narrator`. The `Narrator` component interfaces with the external `neutts-air Model` to convert each text chunk into an audio segment.
    *   As audio segments are generated, `Oration` adds them to `AudioComposition`. `AudioComposition` collects these segments and ensures the total audio size does not exceed limits, raising an `AudioTooLargeError` if it does, which is again caught and displayed by the `AppUI`.
    *   Finally, `AudioComposition` concatenates all segments and saves the final output as a `.wav` file.
4.  **Output:** The `AppUI` provides a audio play for the user to hear their narrated text.


## User Interface (UI) Module

Responsible for all user interaction. A simple web-based interface handles file uploads, displays status messages, and tells the user where their output audio file is located. The UI instantiates a new `Oration` object for each conversion job. The UI then interacts with an `Oration` object to start the process and monitor its state.

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

## Error Handling Strategy

The application uses a straightforward error handling strategy to ensure robustness and provide clear feedback to the user.

*   **Custom Exceptions:** Predictable errors, such as invalid file types or exceeding size limits, are handled using custom exceptions defined in `src/ronda_reade/exceptions.py`. The primary custom exceptions are:
    *   `InvalidTextFileError`: Raised by the `UserText` class during validation if the input file is empty, too large, has an incorrect encoding, or contains overly long words.
    *   `AudioTooLargeError`: Raised by the `AudioComposition` class if adding a new audio segment would cause the final file to exceed its 2 GB size limit.

*   **Exception Propagation:** These specific exceptions are raised by the core service classes (`UserText`, `AudioComposition`). The `Oration` class does not catch these exceptions; it allows them to propagate upwards.

*   **UI-Layer Handling:** All exceptions are caught within the UI layer, specifically in the `AppUI._run_process` method. A `try...except` block wraps the call to `oration.run()`. This block catches the specific custom exceptions as well as any other unexpected `Exception`.

*   **User Feedback:** When an exception is caught, its message is used to update the UI, displaying a clear error status to the user. This approach separates the core processing logic from the user interface's presentation of errors.

## Application Entry Point

*   **`src/ronda_reade/main.py`**: The main entry point for the application, responsible for launching the UI and initiating the conversion process. To run the app, execute the following command from the project's root directory:
```bash
poetry run ronda-reade
```

# Directories
* `/docs`          - Holds all the human-readable documentation.
* `/model`         - Holds the `neuphonic/neutts-air` model files.
