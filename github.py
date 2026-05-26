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

    headers = {}
    if token and token != "your_token_here":
        headers["Authorization"] = f"Bearer {token}"

    repo_response = httpx.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers=headers,
        timeout=20
    )
    repo_response.raise_for_status()
    default_branch = repo_response.json().get("default_branch", "main")

    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1"
    response = httpx.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()

    files = []

    for item in data["tree"]:

        if item["type"] == "blob":
            files.append(item["path"])

    return files
