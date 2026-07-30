# src/llm/client.py
import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


class GeminiClient:
    """Wrapper around the Gemini API."""

    def __init__(self) -> None:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. Please configure your .env file."
            )

        genai.configure(api_key=api_key)

        model_name = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash",
        )

        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str) -> str:
        """Generate Markdown notes from a prompt."""

        response = self.model.generate_content(prompt)

        return response.text

