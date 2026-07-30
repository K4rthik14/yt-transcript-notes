"""Gemini API client wrapper."""

import os
from dotenv import load_dotenv
import google.generativeai as genai

from src.utils.constant import (
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
)

load_dotenv()


class GeminiClient:
    """Wrapper around the Gemini API with configurable parameters."""

    def __init__(self) -> None:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. Please configure your .env file."
            )

        genai.configure(api_key=api_key)

    def generate(
        self,
        prompt: str,
        model_name: str = DEFAULT_MODEL,
        temperature: float = DEFAULT_TEMPERATURE,
        max_output_tokens: int = DEFAULT_MAX_TOKENS,
    ) -> str:
        """
        Generate text content from Gemini model.

        Args:
            prompt: The full prompt string.
            model_name: Name of the Gemini model.
            temperature: Sampling temperature (0.0 to 1.0).
            max_output_tokens: Maximum tokens in response.

        Returns:
            Generated text content.

        Raises:
            RuntimeError: If Gemini API fails.
        """
        try:
            model = genai.GenerativeModel(model_name)
            config = genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_output_tokens,
            )
            response = model.generate_content(prompt, generation_config=config)
            return response.text
        except Exception as e:
            raise RuntimeError(f"Gemini API Error: {e}") from e
