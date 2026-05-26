# github.py

import httpx
from dotenv import load_dotenv
import os
from urllib.parse import urlparse


load_dotenv()


def fetch_repo_tree(repo_url: str):

    parsed = urlparse(repo_url)
    parts = parsed.path.strip("/").split("/")

    if len(parts) < 2:
        raise ValueError("Invalid GitHub repository URL")

    owner = parts[0]
    repo = parts[1].removesuffix(".git")

    token = os.getenv("GITHUB_TOKEN")

    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/HEAD?recursive=1"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = httpx.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    files = []

    for item in data["tree"]:

        if item["type"] == "blob":
            files.append(item["path"])

    return files
