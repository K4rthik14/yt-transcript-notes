# YT Transcript Notes

> Convert YouTube transcripts into clean, structured, Obsidian-ready Markdown notes using AI.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Markdown](https://img.shields.io/badge/Output-Markdown-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

Long YouTube videos often contain valuable knowledge, but reviewing lengthy transcripts is time-consuming.

**YT Transcript Notes** transforms raw transcripts into structured, AI-generated Markdown notes that are easy to read, revise, and save inside tools like Obsidian.

Whether you're studying from tutorials, technical talks, lectures, or podcasts, this tool helps you convert hours of content into concise, organized notes in seconds.

---

## Features

### MVP

- Paste YouTube transcript
- Generate AI-powered notes
- Multiple note styles
- Obsidian-ready Markdown
- Copy generated notes
- Download as `.md`

---

## Planned Features

### Version 1.1

- Auto title generation
- YAML Frontmatter
- Tags
- Key Takeaways
- Definitions
- Action Items

### Version 1.2

- Flashcards
- Mermaid Mind Maps
- Obsidian Internal Links
- Custom Prompt Templates

### Version 2

- YouTube URL support
- Upload transcript files
- PDF support
- Podcast transcripts
- Batch processing
- Ollama / Local LLM support

---

# Demo Workflow

```
Paste Transcript
        │
        ▼
Select Note Style
        │
        ▼
Choose AI Model
        │
        ▼
Generate Notes
        │
        ▼
Markdown Output
        │
        ▼
Download .md
```

---

# Example Output

```md
# Transformers Explained

## Summary

Transformers process sequences using self-attention rather than recurrence.

---

## Key Concepts

- Self Attention
- Positional Encoding
- Multi Head Attention
- Feed Forward Networks

---

## Definitions

### Self Attention

Allows every token to attend to every other token.

---

## Key Takeaways

- Parallel processing
- Better long-range context
- Foundation of modern LLMs

---

## Action Items

- Read Attention Is All You Need
- Implement Self Attention
```

---

# Project Structure

```
yt-transcript-notes/
│
├── app.py
│
├── prompts/
│   ├── study.md
│   ├── summary.md
│   ├── cheat_sheet.md
│   ├── atomic.md
│   └── flashcards.md
│
├── templates/
│   └── obsidian.md
│
├── output/
│
├── assets/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Tech Stack

- Python
- Streamlit
- OpenAI / Gemini / OpenRouter
- Markdown
- Obsidian

---

# Note Styles

## Study Notes

Well-structured notes for revision.

---

## Summary

High-level overview.

---

## Cheat Sheet

Compact quick-reference notes.

---

## Atomic Notes

Small reusable knowledge chunks.

---

## Flashcards *(Coming Soon)*

Question and answer format for active recall.

---

# Why This Project?

Most AI note-taking tools generate generic summaries.

This project focuses on a specific workflow:

> **YouTube Transcript → Structured Markdown Notes**

Designed for:

- Students
- AI Engineers
- Software Developers
- Self-learners
- Researchers

The generated notes are immediately usable inside Obsidian or any Markdown editor.

---

# Roadmap

## MVP

- [x] Paste transcript
- [x] Multiple note styles
- [x] Markdown generation
- [x] Download Markdown

## Next

- [ ] Auto-generated titles
- [ ] YAML Frontmatter
- [ ] Tags
- [ ] Key Takeaways
- [ ] Definitions
- [ ] Action Items

## Future

- [ ] Flashcards
- [ ] Mermaid diagrams
- [ ] YouTube URL support
- [ ] Transcript uploads
- [ ] PDF support
- [ ] Podcast transcripts
- [ ] Batch processing
- [ ] Local LLM support (Ollama)

---

# Future Ideas

- Knowledge Graph generation
- Timeline extraction
- Concept dependency maps
- Quiz generation
- Interview questions
- Semantic search
- Notion export
- PDF export
- Daily learning summaries

---

# Installation

```bash
git clone https://github.com/<username>/yt-transcript-notes.git

cd yt-transcript-notes

pip install -r requirements.txt

streamlit run app.py
```

---


---

# Inspiration

Built for learners who spend hours watching technical YouTube videos and want high-quality, AI-generated Markdown notes without manual formatting.

---

## Star the Repository ⭐

If this project helps you learn faster, consider giving it a ⭐ to support future development.