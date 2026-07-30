"""Application constants and default configuration values."""

GEMINI_MODELS: list[str] = [
    "gemini-2.5-flash",
    "gemini-2.5-pro",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
]

DEFAULT_MODEL: str = "gemini-2.5-flash"
DEFAULT_TEMPERATURE: float = 0.7
DEFAULT_MAX_TOKENS: int = 4096

MIN_TRANSCRIPT_LENGTH: int = 50

NOTE_STYLES: list[str] = [
    "Study Notes",
    "Summary",
]
