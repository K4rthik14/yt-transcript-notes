"""Note generator service using Gemini LLM."""

from src.llm.client import GeminiClient
from src.services.prompt_loader import load_prompt
from src.utils.constant import (
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
)


class NoteGenerator:
    """Generate notes from transcripts."""

    def __init__(self) -> None:
        self.client = GeminiClient()

    def generate(
        self,
        transcript: str,
        note_style: str,
        model_name: str = DEFAULT_MODEL,
        temperature: float = DEFAULT_TEMPERATURE,
        max_output_tokens: int = DEFAULT_MAX_TOKENS,
    ) -> str:
        """
        Generate Markdown notes from transcript.

        Args:
            transcript: Raw transcript text.
            note_style: Selected note style name.
            model_name: Gemini model name.
            temperature: Sampling temperature.
            max_output_tokens: Token output limit.

        Returns:
            Generated Markdown notes.
        """
        template = load_prompt(note_style)

        prompt = template.replace(
            "{{transcript}}",
            transcript,
        )

        markdown = self.client.generate(
            prompt=prompt,
            model_name=model_name,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

        return markdown
