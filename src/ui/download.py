"""Download button UI component."""

import streamlit as st


def render_download_button(
    markdown: str, filename: str = "notes.md"
) -> None:
    """
    Render markdown download button.

    Args:
        markdown: Content string to download.
        filename: Target download filename.
    """
    st.download_button(
        label="⬇️ Download Markdown",
        data=markdown,
        file_name=filename,
        mime="text/markdown",
        use_container_width=True,
    )
