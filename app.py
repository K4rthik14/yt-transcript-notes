import streamlit as st

# UI Components
from src.ui.sidebar import render_sidebar
from src.ui.transcript_input import render_transcript_input
from src.ui.output import render_output


def initialize_session_state() -> None:
    """Initialize Streamlit session state."""

    defaults = {
        "generated_notes": "",
        "selected_style": "Study Notes",
        "transcript": "",
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

    # Sidebar
    render_sidebar()

    # Transcript Input
    render_transcript_input()

    st.divider()

    # Generated Notes
    render_output()


if __name__ == "__main__":
    main()