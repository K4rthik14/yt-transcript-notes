"""Streamlit application main entry point."""

import streamlit as st

# UI Components
from src.ui.output import render_output
from src.ui.sidebar import render_sidebar
from src.ui.transcript_input import render_transcript_input
from src.utils.constant import (
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
)


def initialize_session_state() -> None:
    """Initialize default Streamlit session state variables."""
    defaults = {
        "generated_notes": "",
        "selected_style": "Study Notes",
        "selected_model": DEFAULT_MODEL,
        "temperature": DEFAULT_TEMPERATURE,
        "max_tokens": DEFAULT_MAX_TOKENS,
        "youtube_url": "",
        "transcript": "",
        "is_generating": False,
        "view_mode": "Preview",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def main() -> None:
    """Application entry point."""
    st.set_page_config(
        page_title="YT Transcript Notes",
        page_icon="📝",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    initialize_session_state()

    st.title("📝 YT Transcript Notes")
    st.caption(
        "Convert YouTube transcripts into clean, structured Markdown notes using AI."
    )

    # Sidebar Settings
    render_sidebar()

    # Transcript Input Section
    render_transcript_input()

    st.divider()

    # Generated Notes Output Section
    render_output()


if __name__ == "__main__":
    main()