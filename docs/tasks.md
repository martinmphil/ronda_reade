# Guiding Principle
At each step, the next requirement to be tackled is logically identified and then implemented via the smallest verifiable changes necessary to fulfil it. Rather than a rigid plan, the task list below is intended to be a flexible guide.

# Active Tasks

## Building the Processing Pipeline
*Goal: Expand the skeleton to handle file I/O and the logic from the requirements.*

*   **Implement Text File Input:** Read text from a user-specified file instead of a hard-coded string.
*   **Write Unit Test for Text Chunking:** Create a test to verify that text is correctly segmented based on the rules in `requirements.md`.
*   **Implement Text Chunking:** Segment the input text according to the rules in `requirements.md`.
*   **Implement Conversion Loop:** Create the orchestration logic to loop through text chunks, convert each to audio, and hold them in memory.
*   **Write Unit Test for Audio Concatenation:** Create a test to verify that multiple audio segments are combined correctly into a single audio object.
*   **Implement Audio Concatenation:** Combine the individual audio chunks into a single audio object and write it to a final output file.

## Assess audio flow
*Goal: ensure well-paced smooth audio*

Determine if pauses are required between audio chunks. 

## User Interface
*Goal: Create a simple interface for a user to interact with the application.*

*   **Research and Select UI Library:** Assess `Gradio`, `Streamlit`, or another suitable library.
*   **Build Initial UI:** Develop a minimal interface for file selection, triggering the conversion, and indicating progress.

## Backlog (Future Tasks)
*These are important tasks that can be prioritised and refined as the core application takes shape.*

*   **Validation & Error Handling:** Implement the specific validation rules from `requirements.md` (file size, encoding, etc.).
*   **Configuration:** Add configuration for default directories, etc.


# Completed Tasks

## Environment
Set up Python Poetry environment. 

## Determine Initial Requirements
In `requirements.md` define the initial requirements for this app using "Easy Approach to Requirements Syntax" ([EARS](https://alistairmavin.com/ears/)).

## Local AI Files
Clone the `neutts-air` model code into a directory named `neutts-air` within a `model` directory at the root of this project. 

Running the `neutts-air` process for the first time on a machine triggers the downloading of AI files into a local cache managed by Hugging Face. 

## Core Functionality Spike (The Walking Skeleton)
*Goal: Prove we can convert a simple, hard-coded string to a playable audio file.*

*   **Research `neutts-air`:** Understand the model's API and dependencies.
*   **Create a Basic Narration Script:** Write a single script that:
    *   Takes a hard-coded text string (e.g., "Life, love and happiness.").
    *   Uses the `neutts-air` model to generate audio.
    *   Saves the output as a `sound.wav` file.


