# Guiding Principle
At each step, the next requirement to be tackled is logically identified and then implemented via the smallest verifiable changes necessary to fulfil it. Rather than a rigid plan, the task list below is intended to be a flexible guide.

# Active Tasks

## Progress indicator
Fulfil the requirement that, while the text-to-speech conversion job is running, the app shall provide the user with a visual progress indicator. 

## Assess audio flow
*Goal: ensure well-paced smooth audio*

*   Determine if pauses are required between audio chunks. This can be a feature of the `AudioComposition` class.

## Backlog (Future Tasks)
*These are important tasks that can be prioritised and refined as the core application takes shape.*
*   **Error Handling:** Implement the specific validation rules from `requirements.md`.
*   **Acceptance criteria :** Implement remaining unfulfilled requirements from `requirements.md`.
*   **Configuration:** Add configuration for default directories, etc.
*   **File location:** Offer users a choice of output audio file location.

# Completed Tasks

## Environment
Set up Python Poetry environment. 

## Determine Initial Requirements
In `requirements.md` define the initial requirements for this app using "Easy Approach to Requirements Syntax" ([EARS](https://alistairmavin.com/ears/)).

## Local AI Files
Clone the `neutts-air` model code into a directory named `neutts-air` within a `model` directory at the root of this project. 

Running the `neutts-air` process for the first time on a machine triggers the downloading of AI files into a local cache managed by Hugging Face. 

## Core Functionality Spike (The Walking Skeleton)
*Goal: Show a simple conversion of a hard-coded string to a playable audio file.*

*   **Research `neutts-air`:** Understand the model's API and dependencies.
*   **Create a Basic Narration Script:** Write a single script that:
    *   Takes a hard-coded text string (e.g., "This is a text to speech test.").
    *   Uses the `neutts-air` model to generate audio.
    *   Saves the output as a `sound.wav` file.

## Implement Object-Oriented Structure
*Goal: Create a robust, class-based architecture.*

*   **Define Core Classes:**
    *   Create the class structure for `UserText`, `TextChunker`, `Narrator`, `AudioComposition`, and `Oration`.
*   **Implement `UserText` Class:**
    *   Add methods to read a text file.
    *   Write unit tests for validation logic (file size, encoding, empty file, word length).
    *   Implement the `validate()` method to perform all checks.
*   **Implement `TextChunker` Class:**
    *   Write a unit test to verify text is correctly segmented based on the rules in `requirements.md`.
    *   Implement the `chunk()` method.
*   **Implement `Narrator` Class:**
    *   Write a unit test for narration process.
    *   Implement the logic and imports to convert text into an audio array.
*   **Implement `Oration` Class:**
    *   Develop the `run()` method to orchestrate the process: `UserText` validation, `TextChunker` chunking, and looping.
    *   Integrate the `Narrator` to convert text chunks to audio segments and hold them in memory.
*   **Implement `AudioComposition` Class:**
    *   Write a unit test for audio concatenation.
    *   Implement the logic to combine audio segments and write it to a final `.wav` file.

## User Interface
*Goal: Create a simple interface for a user to interact with the application.*
*   **Research and Select UI Library:** Assessed `Gradio` and `Streamlit`, selecting `Gradio` as the most suitable library for its robust handling of long-running batch processes and features tailored to ML workflows.
*   **Add Gradio Dependency:** Add `gradio` to the project's `pyproject.toml`.
*   **Create UI Module:** Create a new file `src/ronda_reade/ui.py` for the Gradio interface.
*   **Implement Basic UI:** Use `gradio.Blocks` to create the UI with file input, an output audio component, and a "Start" button.
*   **Integrate `Oration`:** Connect the UI to the `Oration` class to run the text-to-speech process.
*   **Update Entry Point:** Modify `src/ronda_reade/main.py` to launch the Gradio app.

## Output file size limit
Limit audio file size to 2 GB.