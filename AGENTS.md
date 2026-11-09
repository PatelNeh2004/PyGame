# Pygame Learning Project Notes

## Goal

Learn Python and Pygame by building a small Hill Climb Racing-style 2D game incrementally.

## Environment

- Run Python with `python3`.
- Always use a project virtual environment named `.venv`.
- Install packages with `python3 -m pip`, so pip matches the active Python.
- Keep dependencies minimal; record runtime packages in `requirements.txt`.

## Standard commands

```sh
python3 --version
python3 -m pip --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pygame
python -m pip freeze > requirements.txt
python main.py
deactivate
```

## Learning order

1. Python CLI and files
2. Virtual environments and pip
3. Pygame window, event loop, drawing, and timing
4. Vehicle physics and terrain
5. Camera, UI, sound, menus, and packaging
6. Git, GitHub CLI, and collaboration basics
7. Neovim editing workflow

## Teaching rule: master one new thing at a time

Whenever a new command, tool, library, or programming concept is introduced, teach it as a small lesson before depending on it:

1. What it is
2. Why we use it in this project
3. How it works internally at a beginner-friendly level
4. The exact commands or code to use
5. Benefits and drawbacks, including when not to use it
6. A tiny hands-on exercise
7. A quick check that proves it worked

Do not rush from virtual environments into pip. First make sure the learner understands what `.venv` contains, activation versus deactivation, why isolation matters, and how to verify which Python is active. Then begin the pip lesson with the same structure: install, inspect, upgrade, uninstall, and save dependencies.

Use plain language and define jargon. Prefer one concept and one short command sequence per lesson. After each lesson, ask whether the learner wants to try the exercise or continue, unless the learner has explicitly asked for a complete walkthrough.

## Strict user-confirmation rule

- Before performing any new action, explain what it will do and why it is needed.
- Show the exact command, code, or file contents before running or creating it.
- Wait for the learner to confirm that they understand and want to proceed.
- Never silently create files, initialize Git, install packages, edit configuration, publish a repository, or make external changes.
- If an action contains multiple new concepts, split it into separate lessons and confirm each part.
- Reading and checking already-requested setup is allowed; writing or changing anything requires this teach/show/confirm step.

## Coding conventions

- Prefer small, runnable steps.
- Explain the Python concept before introducing it.
- Keep the first version simple: one file is fine; split into modules when it becomes useful.
- Do not add a dependency unless the standard library or Pygame cannot reasonably solve the problem.
- Test each change by running the game or a focused command.

## GitHub and Neovim rules

- Use GitHub only through the CLI (`git` and `gh`); do not depend on a web browser for project operations.
- Teach Git and GitHub as separate concepts: local history first, then remotes, pushes, pulls, branches, and pull requests.
- Before creating a remote repository, verify the folder, Git status, GitHub account, repository name, visibility, and remote URL.
- Never commit `.venv`, secrets, tokens, caches, or generated files. Add a `.gitignore` before the first commit.
- Use Neovim (`nvim`) for editing project files and teach only the commands needed for the current task.
- Explain each new Git, GitHub CLI, or Neovim concept using the same seven-step master-first teaching rule.

## Current status

- Python 3.14.6 detected.
- pip 26.1.2 detected.
- `venv` is available.
- Pygame 2.6.1 is installed in `.venv`.
- Completed: virtual environments (`venv`), activation with `source`, verification, and `deactivate`.
- Completed: pip basics (`--version`, `list`, `install`, and `show`).
- Completed: dependency records with `requirements.txt`.
- Completed: GitHub CLI authentication with SSH; account `PatelNeh2004` verified.
- Completed: Git author identity configured with `user.name` and `user.email`.
- Completed: `.gitignore` created and verified with Neovim; `.venv` and generated files are excluded.
- Completed: local Git repository initialized with `git init`; `main` branch verified.
- Current lesson: staging files and creating the first local commit, using Neovim for editing.
