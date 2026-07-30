import streamlit as st

from src.llm.generator import NoteGenerator


def render_transcript_input() -> None:
    """Render transcript input section."""

    st.subheader("📄 Transcript")

    transcript = st.text_area(
        label="Paste your YouTube transcript",
        value=st.session_state.transcript,
        height=350,
        placeholder="Paste the transcript here...",
    )

    st.session_state.transcript = transcript

    col1, col2 = st.columns([1, 4])

    with col1:
        generate = st.button(
            "✨ Generate Notes",
            use_container_width=True,
        )

    with col2:
        word_count = len(transcript.split())
        st.caption(f"Words: {word_count}")

    if generate:
        if not transcript.strip():
            st.warning("Please paste a transcript first.")
            return

        try:
            generator = NoteGenerator()

            with st.spinner("Generating notes..."):
                markdown = generator.generate(
                    transcript=transcript,
                    note_style=st.session_state.selected_style,
                )

            st.session_state.generated_notes = markdown

        except Exception as e:
            st.error(f"Error: {e}")