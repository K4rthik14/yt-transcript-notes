"""Transcript input section UI component."""

import streamlit as st

from src.llm.generator import NoteGenerator
from src.services.youtube import fetch_transcript_from_url
from src.utils.constant import MIN_TRANSCRIPT_LENGTH
from src.utils.helper import calculate_text_stats


def render_transcript_input() -> None:
    """Render YouTube URL fetch input, transcript text area, text stats, and actions."""
    with st.container():
        st.subheader("📄 Transcript")

        # YouTube URL Input Section
        yt_col_input, yt_col_btn = st.columns([3, 1])

        with yt_col_input:
            yt_url = st.text_input(
                label="YouTube URL (Optional)",
                value=st.session_state.youtube_url,
                placeholder="https://www.youtube.com/watch?v=...",
                disabled=st.session_state.is_generating,
            )
            st.session_state.youtube_url = yt_url

        with yt_col_btn:
            st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
            fetch_clicked = st.button(
                "📥 Fetch Transcript",
                use_container_width=True,
                disabled=st.session_state.is_generating,
            )

        if fetch_clicked:
            if not yt_url.strip():
                st.warning("Please enter a YouTube URL first.")
            else:
                try:
                    with st.spinner("Fetching YouTube transcript..."):
                        fetched_text = fetch_transcript_from_url(yt_url)
                    st.session_state.transcript = fetched_text
                    st.toast("Transcript fetched successfully!", icon="✅")
                    st.rerun()
                except Exception as e:
                    st.error(f"Failed to fetch transcript: {e}")

        # Transcript Text Area
        transcript = st.text_area(
            label="Paste your YouTube transcript",
            value=st.session_state.transcript,
            height=350,
            placeholder="Paste the transcript here...",
            key="transcript_text_area",
            disabled=st.session_state.is_generating,
        )

        st.session_state.transcript = transcript

        char_count, word_count = calculate_text_stats(transcript)

        col_action, col_clear, col_stats = st.columns([2, 2, 3])

        with col_action:
            generate_disabled = st.session_state.is_generating
            generate_clicked = st.button(
                "✨ Generate Notes",
                use_container_width=True,
                disabled=generate_disabled,
                type="primary",
            )

        with col_clear:
            clear_clicked = st.button(
                "🗑️ Clear Transcript",
                use_container_width=True,
                disabled=st.session_state.is_generating or not transcript,
            )

        with col_stats:
            st.caption(f"📊 **Characters:** {char_count:,} | **Words:** {word_count:,}")

        if clear_clicked:
            st.session_state.transcript = ""
            st.rerun()

        if generate_clicked:
            clean_text = transcript.strip()

            if not clean_text:
                st.warning("Please paste a transcript first.")
                return

            if len(clean_text) < MIN_TRANSCRIPT_LENGTH:
                st.warning(
                    f"Transcript is too short. Minimum requirement is {MIN_TRANSCRIPT_LENGTH} characters "
                    f"(currently {len(clean_text)} characters)."
                )
                return

            st.session_state.is_generating = True

            try:
                generator = NoteGenerator()

                with st.spinner("✨ Transforming transcript into structured notes..."):
                    markdown = generator.generate(
                        transcript=clean_text,
                        note_style=st.session_state.selected_style,
                        model_name=st.session_state.selected_model,
                        temperature=st.session_state.temperature,
                        max_output_tokens=st.session_state.max_tokens,
                    )

                st.session_state.generated_notes = markdown
                st.toast("Notes generated successfully!", icon="✅")

            except Exception as e:
                st.error(f"Failed to generate notes: {e}")

            finally:
                st.session_state.is_generating = False