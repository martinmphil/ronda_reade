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
                output_audio = gr.Audio(label="Output Audio", type="filepath")

            start_button = gr.Button("Convert text to speech")

            start_button.click(
                fn=self._run_process,
                inputs=[input_text_file],
                outputs=[output_audio],
                api_name="narrate",
                show_progress="full",
            )

        return app

    def _run_process(self, text_file, progress=gr.Progress(track_tqdm=True)):
        """
        Runs the text-to-speech process when the button is clicked.
        """
        if text_file is None:
            return gr.Audio(
                value=None,
                label="Error: No file provided. Please upload a text file.",
                visible=True,
            )

        input_path = Path(text_file.name)
        oration = Oration(input_path=input_path)
        output_path = oration.run(progress=progress)

        return gr.Audio(value=str(output_path), label="Narration Complete", visible=True)

    def launch(self):
        """Launches the Gradio application."""
        self._app.launch()


if __name__ == "__main__":
    ui = AppUI()
    ui.launch()
