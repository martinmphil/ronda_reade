"""Main entry point for the Ronda Reade application."""

from ronda_reade.ui import AppUI


def run():
    """Launches the user interface for the application."""
    ui = AppUI()
    ui.launch()


if __name__ == "__main__":
    run()