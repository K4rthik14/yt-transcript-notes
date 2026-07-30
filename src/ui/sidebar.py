
import streamlit as st


NOTE_STYLES = [
    "Study Notes",
    "Summary",
]


def render_sidebar() -> None:
    """Render the application sidebar."""

    with st.sidebar:
        st.header("⚙️ Settings")

        st.session_state.selected_style = st.selectbox(
            "Note Style",
            options=NOTE_STYLES,
            index=NOTE_STYLES.index(st.session_state.selected_style),
            help="Choose how the transcript should be transformed.",
        )

        st.divider()

        st.markdown("### About")
        st.write(
            "Convert YouTube transcripts into structured, "
            "Obsidian-ready Markdown notes using AI."
        )

        st.divider()

        st.caption("🚀 Built with Streamlit + Gemini")

