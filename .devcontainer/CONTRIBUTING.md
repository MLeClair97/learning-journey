# Contributing Guidelines

This guide explains how to make commits and push changes so the Git history stays clear and professional.

---

## 1. Branches
- Work on the **`main`** branch unless adding large features or experiments.
- Use descriptive branch names for features or fixes:
  - `feature/sqlite-setup`
  - `fix/streamlit-port-forward`

---

## 2. Commit Messages

### Format

Verb: <short description in imperative, ≤72 chars>

optional body: <why + what changed (bullets ok)>

Refs: <issue/PR>

### Verbs
- **Add** – new feature, file, or data
- **Fix** – bug or issue resolution
- **Update** – modify existing behavior/content
- **Refactor** – restructure code without changing behavior
- **Docs** – documentation changes only
- **Chore** – tooling, dependencies, configs
- **Test** – adding or updating tests

**Examples**
- `Add SQLite seed script and DB helper`
- `Fix pandas import error in Codespace`
- `Docs: explain devcontainer setup`

---

## 3. Workflow
1. Pull latest changes:
   ```bash
   git pull origin main
2. Make your changes.
3. Stage changes in VS Code or with:
    ```bash 
    git add . ```
4. Commit with a clear message:
    ```bash
    git commit -m "Add Streamlit test app for Codespace verification"
5. Push to GitHub:
    ```bash
    git push origin main

### 4. Code Style

- Follow Python PEP 8 style where practical.
- Keep functions focused; prefer clear names over clever shortcuts.
- Commit small, logical chunks rather than one huge commit.

### 5. Environment

- This project uses a **Dev Container** for consistency.

All dependencies should be listed in `week-04-integrations/Day_14_AI_Sales_Analytics_Platform/requirements.txt`.

Keep `.env` variables minimal and documented.
