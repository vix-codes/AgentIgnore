# AgentIgnore

AgentIgnore helps you create a `.agentignore` file for a GitHub repository.

That file tells coding agents which parts of a project are probably not worth reading, such as build folders, logs, lock files, cache folders, and other noisy files. The goal is simple: give an AI coding agent less clutter so it can focus on the files that actually matter.

## Why This Exists

Modern code repositories can get messy fast. They often contain generated files, temporary files, build output, dependency folders, and other files that are not useful when an AI coding assistant is trying to understand the project.

AgentIgnore gives you a quick starting point. Paste a GitHub repository link, generate an ignore file, review it, and save it into your project.

## What It Does

- Accepts a GitHub repository URL.
- Reads the repository file list.
- Automatically filters common noisy files and folders.
- Optionally asks Gemini to suggest extra files that may not be useful for coding-agent context.
- Shows the generated `.agentignore` content in the browser.
- Lets you copy or download the file.

## BYOK: Bring Your Own Key

AgentIgnore uses a BYOK model, which means **Bring Your Own Key**.

You use your own API keys locally:

- A GitHub token is used to read repository file trees.
- A Gemini API key is used only if you want AI-assisted filtering.

Your keys are not included in the project and should not be uploaded to GitHub. Keep them in your local `.env` file.

If you do not add a valid Gemini key, the app still works with the basic rule-based filter. It just skips the AI suggestions.

## Who It Is For

AgentIgnore is useful for:

- Developers using AI coding tools.
- Students working with large GitHub projects.
- People who want cleaner repository context.
- Anyone who wants a quick `.agentignore` starter file without manually scanning every folder.

## How To Use It

1. Start the app on your computer.
2. Open the local web page.
3. Paste a GitHub repository URL.
4. Click **Generate**.
5. Review the result.
6. Copy or download the `.agentignore` file.
7. Put it in the root of the project where you want to use it.

## Local Setup

Install the required Python packages:

```powershell
py -3.12 -m pip install -r requirements.txt
```

Create a `.env` file in the project folder:

```env
GITHUB_TOKEN=your_github_token_here
GEMINI_API_KEY=your_gemini_key_here
```

The Gemini key is optional. If you leave it out, AgentIgnore still runs with basic filtering.

Start the app:

```powershell
py -3.12 -m uvicorn main:app --reload
```

Open this in your browser:

```text
http://127.0.0.1:8000/
```

Do not open `static/index.html` directly from your file browser. The page needs the local FastAPI server so it can call the generator.

## Notes

AgentIgnore is meant to create a starting point, not a perfect final answer. Always review the generated file before using it in an important project.

The app runs locally. It is intentionally small and simple.

