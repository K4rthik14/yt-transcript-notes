"""Sidebar UI component for app settings and information."""

import streamlit as st

from src.utils.constant import GEMINI_MODELS, NOTE_STYLES


def render_sidebar() -> None:
    """Render application settings and controls in the sidebar."""
    with st.sidebar:
        st.header("⚙️ Settings")

        st.subheader("Model Configuration")

        model_index = (
            GEMINI_MODELS.index(st.session_state.selected_model)
            if st.session_state.selected_model in GEMINI_MODELS
            else 0
        )

        st.session_state.selected_model = st.selectbox(
            "Gemini Model",
            options=GEMINI_MODELS,
            index=model_index,
            help="Select the Gemini model to use for notes generation.",
        )

        st.session_state.temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=float(st.session_state.temperature),
            step=0.05,
            help="Higher values make output more creative, lower values more deterministic.",
        )

        st.session_state.max_tokens = st.slider(
            "Max Output Tokens",
            min_value=512,
            max_value=8192,
            value=int(st.session_state.max_tokens),
            step=256,
            help="Maximum length of generated notes in tokens.",
        )

        st.divider()

        st.subheader("Output Configuration")

        style_index = (
            NOTE_STYLES.index(st.session_state.selected_style)
            if st.session_state.selected_style in NOTE_STYLES
            else 0
        )

        st.session_state.selected_style = st.selectbox(
            "Note Style",
            options=NOTE_STYLES,
            index=style_index,
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
