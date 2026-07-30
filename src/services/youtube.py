"""YouTube transcript fetching service using youtube-transcript-api."""

import re
from youtube_transcript_api import (
    CouldNotRetrieveTranscript,
    InvalidVideoId,
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
)


def extract_video_id(url: str) -> str:
    """
    Extract YouTube 11-character video ID from a URL.

    Args:
        url: Full or shortened YouTube URL.

    Returns:
        Extracted video ID string.

    Raises:
        ValueError: If the URL is invalid or video ID cannot be parsed.
    """
    if not url or not url.strip():
        raise ValueError("Please enter a valid YouTube URL.")

    clean_url = url.strip()
    pattern = r"(?:v=|\/|be\/|embed\/|shorts\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, clean_url)

    if match:
        return match.group(1)

    raise ValueError("Invalid YouTube URL format. Could not extract Video ID.")


def fetch_transcript_from_url(url: str) -> str:
    """
    Fetch and extract plain text transcript from a YouTube video URL.

    Args:
        url: YouTube video URL string.

    Returns:
        Joined plain text transcript string.

    Raises:
        ValueError: If URL or video ID is invalid.
        RuntimeError: For transcript fetching or video availability errors.
    """
    video_id = extract_video_id(url)

    try:
        api = YouTubeTranscriptApi()
        transcript_obj = api.fetch(video_id)

        if hasattr(transcript_obj, "snippets"):
            text_snippets = [
                s.text for s in transcript_obj.snippets if hasattr(s, "text")
            ]
        else:
            text_snippets = [
                item.get("text", "")
                for item in transcript_obj
                if isinstance(item, dict)
            ]

        full_text = " ".join(text_snippets).strip()

        if not full_text:
            raise RuntimeError("The transcript for this video is empty.")

        return full_text

    except VideoUnavailable:
        raise RuntimeError(
            "This video is unavailable or cannot be accessed."
        )

    except NoTranscriptFound:
        raise RuntimeError(
            "No transcript is available for this video."
        )

    except TranscriptsDisabled:
        raise RuntimeError(
            "The creator has disabled transcripts for this video."
        )

    except InvalidVideoId:
        raise RuntimeError(
            "Invalid YouTube Video ID."
        )

    except CouldNotRetrieveTranscript:
        raise RuntimeError(
            "Could not retrieve transcript from YouTube."
        )

    except (ValueError, RuntimeError):
        raise

    except Exception as e:
        raise RuntimeError(
            f"Failed to fetch YouTube transcript: {e}"
        )
