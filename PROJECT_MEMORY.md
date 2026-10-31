# IEC FASTAPI BOOK STORE

### Project Memory & Developer Guide

**A beginner-friendly reference for the project**

*Project notes | Working agreements | Current status*

---

> **How to use this guide**
>
> Read this guide before making project changes. Keep important project facts
> and decisions here so they are easy to find. Update this file when those facts
> change.
>
> **Editing boundary:** Update this file only. Do not edit code or other project
> files unless the user explicitly asks.

## Contents

| Section | Topic |
|:--:|---|
| 1 | [Project overview](#1-project-overview) |
| 2 | [Working agreements](#2-working-agreements) |
| 3 | [Project files](#3-project-files) |
| 4 | [Setup and configuration](#4-setup-and-configuration) |
| 5 | [Current code notes](#5-current-code-notes) |
| 6 | [Progress and verification](#6-progress-and-verification) |
| 7 | [Unknowns and protected information](#7-unknowns-and-protected-information) |

---

## 1. Project overview

| **Project detail** | **Information** |
|---|---|
| Project name | IEC-FastApi-Book-store-App |
| Purpose | Beginner FastAPI book-store practice project |
| Main language | Python |
| Python environment present | `3.12.13` |
| Database tools | SQLAlchemy and PostgreSQL |
| Dependencies | [`requirements.txt`](./requirements.txt) |

This is a practice project. Do not treat features that are not present in the
inspected source files—such as authentication, API routes, or deployment—as
requirements.

## 2. Working agreements

### Writing and documentation

- Use clear, beginner-friendly language.
- Function docstrings should state expected input, output, what the function
  does, and why it is needed.
- Add concise module and class docstrings where appropriate.
- Use comments to explain purpose or non-obvious behavior. Avoid comments that
  merely repeat the code.

### Code and changes

- Review relevant code when useful, but **do not modify coding files** unless
  the user explicitly asks.
- Update only `PROJECT_MEMORY.md` by default.
- Preserve existing behavior; do not make assumptions about requirements.
- Ask questions only when important information is genuinely missing.

### Memory and privacy

- Keep meaningful project decisions and status current in this guide.
- Avoid duplicate or temporary notes.
- Never copy database credentials or other `.env` values into documentation,
  chat, or source code.

## 3. Project files

| **File** | **Purpose** |
|---|---|
| [`db.py`](./db.py) | Loads database configuration and provides SQLAlchemy setup and database helper functions. |
| [`models.py`](./models.py) | Defines the `Book` database model and its columns. |
| [`schemas.py`](./schemas.py) | Defines Pydantic models for validating book input and output data. |
| [`requirements.txt`](./requirements.txt) | Lists the Python packages used by the project. |
| [`README.md`](./README.md) | Brief project introduction. |
| `.env` | Local settings, including the database URL. Keep secret values private. |

### Database helper reference

| **Function** | **Expected input** | **Output or effect** | **Why it is needed** |
|---|---|---|---|
| `get_db()` | None | Yields a database session, then closes it. | Gives app code temporary database access and cleans up the session afterward. |
| `create_tables()` | None | Creates missing tables described by imported models; returns no value. | Prepares the database to store model data. |

## 4. Setup and configuration

1. The repository contains a Python `3.12.13` environment. In VS Code, confirm
   the selected interpreter when investigating missing imports.
2. Install dependencies from `requirements.txt` into the same environment VS
   Code uses.
3. `db.py` reads `SQLALCHEMY_DATABASE_URL` with `python-dotenv`.
4. `requirements.txt` lists `psycopg2-binary` as a PostgreSQL driver.
5. The current `db.py` passes the URL from `.env` directly to SQLAlchemy. Do not
   assume which PostgreSQL driver the URL selects.

> **Security note:** Database URLs can contain usernames and passwords. Never
> record or share the URL itself.

## 5. Current code notes

These are observations from the current versions of `db.py` and `models.py`.
They are recorded for awareness and are **not permission to change code**.

### `db.py`

- Defines the database engine, SQLAlchemy model base, and session factory.
- `get_db()` yields a database session and closes it in a `finally` block.
- `create_tables()` creates tables defined by imported models.
- Both helper functions have docstrings describing their input, output,
  behavior, and purpose.

### `models.py`

- Defines a `Book` model for the `Books` table.
- The visible columns are `id`, `title`, `description`, `author`, and `year`.
- The import currently uses `from SQLAlchemy import ...` with uppercase
  letters. The package name is lowercase (`sqlalchemy`); this may prevent the
  model from importing.
- `Float` and `DateTime` are imported but are not used in the visible model.
- The intended meaning and data types of every field have not been confirmed.

### `schemas.py`

- Defines `BookBase` with `title`, `description`, `author`, and `year` fields.
- `BookCreate` reuses those fields for incoming book creation data.
- `Book` adds an integer `id` for representing a saved book.
- The module and schema classes have beginner-friendly docstrings explaining
  their expected input, output, and purpose.
- The schema configuration includes `orm_mode` and `from_attributes` to support
  reading values from database model objects.

## 6. Progress and verification

### Completed

- Created this central project guide.
- Recorded beginner-friendly documentation preferences and the memory-file-only
  editing boundary.
- Added documentation to `schemas.py` at the user's request; no schema fields or
  validation behavior were changed.
- Reviewed the current database helper, book model, and schema files for project
  context.

### Not verified

- No project test suite was found among the inspected root files.
- The current code has not been validated by connecting to PostgreSQL or
  creating database tables.
- Any code changes previously undone by the user must stay undone unless the
  user explicitly requests them.

## 7. Unknowns and protected information

- The actual database URL, password, and other private `.env` values are
  intentionally not included.
- The author's intended field types, database migration strategy, production
  settings, and deployment requirements are unknown.
- Do not infer requirements from these unknowns or change code based on guesses.

---

*End of guide*
