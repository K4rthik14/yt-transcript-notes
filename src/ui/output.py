"""Generated notes output section UI component."""

import json
import streamlit as st
import streamlit.components.v1 as components

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
        col_toggle, col_copy, col_clear = st.columns([3, 2, 2])

        with col_toggle:
            view_mode = st.radio(
                "View Mode",
                options=["Preview", "Raw Markdown"],
                horizontal=True,
                index=0 if st.session_state.view_mode == "Preview" else 1,
                key="view_mode_radio",
            )
            st.session_state.view_mode = view_mode

        with col_copy:
            copy_clicked = st.button(
                "📋 Copy Markdown",
                use_container_width=True,
            )

        with col_clear:
            clear_clicked = st.button(
                "🗑️ Clear Generated Notes",
                use_container_width=True,
            )

        if clear_clicked:
            st.session_state.generated_notes = ""
            st.rerun()

        if copy_clicked:
            encoded_notes = json.dumps(st.session_state.generated_notes)
            components.html(
                f"""
                <script>
                navigator.clipboard.writeText({encoded_notes}).then(function() {{
                    console.log('Copied to clipboard');
                }}).catch(function(err) {{
                    console.error('Copy failed', err);
                }});
                </script>
                """,
                height=0,
                width=0,
            )
            st.toast("Markdown copied to clipboard!", icon="📋")

        st.divider()

        # Display Notes
        if st.session_state.view_mode == "Preview":
            st.markdown(st.session_state.generated_notes)
        else:
            st.code(
                st.session_state.generated_notes,
                language="markdown",
            )

        st.divider()

        # Download Section
        filename = generate_filename(st.session_state.generated_notes)
        render_download_button(
            markdown=st.session_state.generated_notes,
            filename=filename,
        )