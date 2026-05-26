# gemini.py

import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


def gemini_filter(files: list):

    if not api_key or api_key == "your_key_here":
        return []
    
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    file_text = "\n".join(files)

    prompt = f"""
You are an AI that helps reduce repository context noise for coding agents.

Below is a list of file paths from a GitHub repository.

Your job:
- Identify files or folders that are probably NOT useful for understanding or editing the main application code.
- Ignore generated files, coverage reports, migrations, seed data, cache files, logs, etc.
- Keep important source code and configs.

Return ONLY a valid JSON array of file paths to ignore.
Do not explain anything.

Files:
{file_text}
"""

    try:
        response = model.generate_content(prompt)
    except Exception:
        return []

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    try:
        ignored_files = json.loads(text)
    except:
        ignored_files = []

    return ignored_files
