# main.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from github import fetch_repo_tree
from filter import rule_based_filter
from gemini import gemini_filter


app = FastAPI()


class RepoRequest(BaseModel):
    repo_url: str


@app.post("/generate")
def generate_agentignore(data: RepoRequest):

    try:
        files = fetch_repo_tree(data.repo_url)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid repo URL or unable to fetch repository"
        )

    ignored_rule, remaining = rule_based_filter(files)

    ignored_ai = gemini_filter(remaining)

    final_ignored = ignored_rule + ignored_ai

    content = "\n".join(final_ignored)

    return Response(
        content=content,
        media_type="text/plain",
        headers={
            "Content-Disposition": "attachment; filename=.agentignore"
        }
    )


app.mount("/", StaticFiles(directory="static", html=True), name="static")
