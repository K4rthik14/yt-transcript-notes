"""Generated notes output section UI component."""

import streamlit as st

from src.ui.download import render_download_button
from src.utils.helper import generate_filename


def render_output() -> None:
    """Render output control toolbar, formatted markdown / raw view, and download options."""
    with st.container():
        st.subheader("📝 Generated Notes")

        if not st.session_state.generated_notes:
            st.info("Your generated Markdown notes will appear here.")
            return

        # Output Action Bar
        col_toggle, col_clear = st.columns([3, 2])

        with col_toggle:
            view_mode = st.radio(
                "View Mode",
                options=["Preview", "Raw Markdown"],
                horizontal=True,
                index=0 if st.session_state.view_mode == "Preview" else 1,
                key="view_mode_radio",
            )
            st.session_state.view_mode = view_mode

        with col_clear:
            clear_clicked = st.button(
                "🗑️ Clear Generated Notes",
                use_container_width=True,
            )

        if clear_clicked:
            st.session_state.generated_notes = ""
            st.rerun()

        st.divider()

        # Display Notes
        if st.session_state.view_mode == "Preview":
            st.markdown(st.session_state.generated_notes)
        else:
            st.code(
                st.session_state.generated_notes,
                language="markdown",
                wrap_lines=True,
            )

        st.divider()

        # Download Section
        filename = generate_filename(st.session_state.generated_notes)
        render_download_button(
            markdown=st.session_state.generated_notes,
            filename=filename,
        )