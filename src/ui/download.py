# src/ui/download.py

import streamlit as st


def render_download_button(markdown: str) -> None:
    """Render markdown download button."""

    st.download_button(
        label="⬇️ Download Markdown",
        data=markdown,
        file_name="notes.md",
        mime="text/markdown",
        use_container_width=True,
    )
