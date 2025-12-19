# Small Design Iterations
Progress in the smallest possible steps. 

Break down all development tasks into the smallest possible increment that is atomic, complete, independently stable and leaves the program in provably functional state.

Each increment should involve only the minimum alterations required to address one single, logical concern. 

Then iterate through a tight loop of: granular change; verification; commit. 

# Modular Design
Compartmentalise software into modules that address one single, distinct concern. 

Each module should be just large enough to perform one independent, clearly defined, function. 

Each module should be internally coherent and encapsulate one specific piece of functionality.

Minimise coupling between modules by using clear, stable, well-defined interfaces between modules. 

# Dev Methodology
Write clean, consistent, simple code that is easy to read and understand.

Adhere to recommended best practices. 

Comply with open, public standards. 

Prioritise open source software. 

Write robust, defensive code that gracefully handles all failure modes, faults and errors. 

Regularly review all docs. 

## Python Virtual Environment
Ensure all operations use the project's isolated virtual environment. Any command executing a Python script or a tool installed within the Poetry environment (like `pytest` or `python`) must be prefixed with `poetry run`. For example, instead of `python`, always use `poetry run python`.

## Relative File Paths
Never hard-code absolute file paths into any project file. Construct all paths dynamically at runtime, relative to the project root directory. This ensures the project is portable and protects the privacy of the local file system structure.

## Test-Driven Development (TDD)
Software should be testable.

Tests should assert falsifiable claims.

A unit test should be written for every desired behaviour.

Write tests first then build up projects from a reliable automated test suit.

Regularly run tests to check for regressions.

# Requirements 
Use "Easy Approach to Requirements Syntax" (EARS) where possible to define and update system requirements. 
See
https://alistairmavin.com/ears/
and
A. Mavin, P. Wilkinson, A. Harwood and M. Novak, "Easy Approach to Requirements Syntax (EARS)," 2009 17th IEEE International Requirements Engineering Conference, Atlanta, GA, USA, 2009, pp. 317-322, doi: 10.1109/RE.2009.9.

# Flexible Documentation
In living documents that evolve with the project (e.g., task lists, design docs), prefer un-ordered lists (bullet points) over numbered lists. This maintains flexibility, allowing for the reordering of items without the need to manually renumber the entire list.

Use a logical heading hierarchy in all Markdown files, starting with `#` for the main title or primary sections. This ensures consistency, improves readability, and allows for a clear document structure.

For task-tracking documents like `docs/tasks.md`, once a task is fully completed, its entire entry (including its heading and all sub-points) should be moved from the active list to the bottom of the dedicated "Completed Tasks" section at the end of the file.

# Code Comments
In code comments, use the active imperative mood (eg set timeout, validate input, fetch data). Exclude all personal pronouns, including 'we'. 

# Language 
Always use British English in documentation and code comments.
