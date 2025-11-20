# User stories 

As a user I want to input a local text file on my home computer to hear a high-quality audio narration of the text using the app's inbuilt voice. 

As a user I want primarily to hear my native language of English in a British English accent. 

As a user I do not normally need multilingual responses. 

# Requirements 

## System constraints 

The app shall be compatible with Python 3.14.0 running locally on a Ubuntu 24.04 Linux home computer. 

The app shall operate within a maximum peak memory usage of 2 GB on the client device. 

## Text input

When the user selects a text file, the app shall convert the user's text file into an audio file. 

The app shall accept one text file as an input for a single text-to-speech run. 

If the input text file is empty, then the app shall reject the file and report a message to the user saying, " This text file is empty. Please provide a file containing plain text. " 

If the app detects an input text file encoding other than UTF-8, then the app shall reject the file and report a message to the user saying, " Please provide a text file containing only plain text. " 

If the input text file size is greater than 5MB (~1 million words), then the app shall reject the file and report a message to the user saying, " This text file is larger than 5 MB. Please provide a plain text file smaller than 5MB. " 

If the input text file contains any word longer than 50 letters, then the app shall reject the file and report a message to the user saying, " This file contains overly long words. Please provide a plain text where all words are shorter than 45 letters. " 

## Text-to-speech 

The app shall synthesise speech. 

The app shall use an inbuilt voice for all speech synthesis. 

The app shall locally convert all the written English in the input text file into an audio narration using a light-weight local neural network. 

The app shall output one audio file for a single text-to-speech run. 

## Audio output 

The app shall ensure the total size of the final output audio file is less than 1GB. 

The app shall set the output file type to ".wav". 

The app shall generate the output audio at a sample rate of 24 kHz ±5%. 

When the app processes an input text file, the app shall segment the text into chunks such that each chunk length is the smallest of 1 paragraph, 5 sentences, or 1000 characters. 

If the app is unable to break the text into valid chunks, then the app shall cease processing and report an error to the user saying, " The app could not process your input text file. Please submit a different plain text file. "

The app shall complete the entire text-to-speech conversion process in less than two hours. 

When the user aborts a text-to-speech conversion job, the app shall leave the output directory in a clean state. 

When a text-to-speech conversion job successfully completes, the app shall save the resulting audio data to an output file in the designated output directory. 

## Directories 
When the user activates the app, the app shall allow the user to select an input text file from any arbitrary location on their file system. 

When the user activates the app, the app shall default to saving the output audio file in the `/tmp/gradio` directory. 

The `/tmp/gradio` directory shall regularly be purged of old files. 

When the user activates the app, the app shall offer the user an option of selecting an output directory for the output audio file at any arbitrary location on their file system. 

When the user selects an output directory, the user-output prompt for the output audio file shall default to the `~/Downloads` directory. 

## Job progressing 
While the text-to-speech conversion job is running, the app shall provide the user with a visual progress indicator. 

While the text-to-speech conversion job is running, the app shall provide the user with an option to abort the job. 

While the text-to-speech conversion job is running, the app shall disable the file selection input to prevent concurrent jobs. 

## Job complete 
When the app successfully saves the audio file, the app shall indicate the job is complete.

## Unexpected errors 
If the app encounters an unhandled exception, then the app shall report an error to the user with a message saying, " An unexpected error occurred. Please try restarting the app. " 


