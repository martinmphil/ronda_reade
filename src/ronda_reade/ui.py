"""This module contains the Gradio user interface for the application."""

import gradio as gr
from pathlib import Path
from ronda_reade.oration import Oration


class AppUI:
    """Encapsulates the Gradio user interface for the application."""

    def __init__(self):
        self._app = self._create_app()

    def _create_app(self):
        """Creates the Gradio Blocks application."""
        with gr.Blocks() as app:
            gr.Markdown("# Ronda Reade")
            gr.Markdown(
                "Convert your text file into an audio narration."
            )
            gr.Markdown(
                "This app saves output audio files to `/tmp/gradio`"
            )

            with gr.Row():
                input_text_file = gr.File(label="Input Text File")
                output_audio = gr.Audio(label="Output Audio", type="filepath", visible=True)

            progress_text = gr.Markdown("Ready to narrate.", visible=True)

            start_button = gr.Button("Convert text to speech")

            start_button.click(
                fn=self._run_process,
                inputs=[input_text_file],
                outputs=[output_audio, progress_text],
                api_name="narrate",
            )

        return app

    def _run_process(self, text_file):
        """
        Runs the text-to-speech process as a generator when the button is clicked,
        yielding text-based progress updates.
        """
        if text_file is None:
            yield gr.update(
                label="Error: No file provided. Please upload a text file.",
                visible=True
            ), gr.update(value="Error: No file provided. Please upload a text file.")
            return

        # Start of the process: ensure audio player is visible but empty
        yield gr.update(value=None, visible=True), gr.update(value="Starting...")

        input_path = Path(text_file.name)
        oration = Oration(input_path=input_path)
        
        output_path = None
        try:
            # The generator yields progress updates (percentage, description)
            oration_generator = oration.run()
            while True:
                try:
                    progress, desc = next(oration_generator)
                    # Format progress into a text string
                    bar_length = 20
                    filled_length = int(bar_length * progress)
                    bar = '█' * filled_length + '-' * (bar_length - filled_length)
                    progress_string = f"[{bar}] {int(progress*100)}% {desc}"
                    yield gr.update(visible=True), gr.update(value=progress_string)

                except StopIteration as e:
                    output_path = e.value # The return value is in the exception
                    break

        except Exception as e:
            yield gr.update(
                label=f"Error: {e}",
                visible=True
            ), gr.update(value=f"An error occurred: {e}")
            return

        yield gr.update(value=str(output_path), label="Narration Complete", visible=True), gr.update(value="Narration Complete.")


    def launch(self):
        """Launches the Gradio application."""
        self._app.launch()


if __name__ == "__main__":
    ui = AppUI()
    ui.launch()
