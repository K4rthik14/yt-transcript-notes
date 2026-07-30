# src/services/prompt_loader.py


from pathlib import Path


PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


PROMPT_FILES = {
    "Study Notes": "study.md",
    "Summary": "summary.md",
}


def load_prompt(note_style: str) -> str:
    """
    Load the prompt template for the selected note style.

    Args:
        note_style: Selected note style.

    Returns:
        Prompt template as a string.

    Raises:
        FileNotFoundError: If the prompt file doesn't exist.
        ValueError: If the note style is unsupported.
    """

    filename = PROMPT_FILES.get(note_style)

    if filename is None:
        raise ValueError(f"Unsupported note style: {note_style}")

    prompt_path = PROMPTS_DIR / filename

    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt not found: {prompt_path}")

    return prompt_path.read_text(encoding="utf-8")