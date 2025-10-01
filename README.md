# Eventator

Eventator is a lightweight Django application crafted for Hacktoberfest 2025 with the Django Cameroon community. It showcases upcoming events and invites contributors to submit new ideas using a Tailwind-powered interface served via CDN.

## Features
- Curated list of published Hacktoberfest events
- Submission form for community-driven event ideas stored as unpublished entries
- Tailwind CSS UI loaded from CDN for quick iteration
- JSON seed data (`data/events.json`) with a custom management command
- SQLite database configured by default

## Prerequisites
- Python 3.10 or later
- [uv](https://github.com/astral-sh/uv) for environment and dependency management

## Installation
```bash
uv sync
```

The first run creates a `.venv` folder managed by uv and installs all project dependencies declared in `pyproject.toml`.

## Database setup
```bash
uv run python manage.py migrate
uv run python manage.py seed_events
```

Use `uv run python manage.py seed_events --draft` to keep seeded entries in the review queue. A different JSON file can be supplied with `--path path/to/custom_events.json`.

## Running the development server
```bash
uv run python manage.py runserver 0.0.0.0:8000
```

Open http://127.0.0.1:8000/ to browse the current events and submit new ideas.

## Tests
```bash
uv run python manage.py test
```

## Tailwind via CDN
Tailwind CSS is bootstrapped using the official CDN helper (`https://cdn.tailwindcss.com`) directly in `events/templates/events/home.html`. No local build tooling is required, keeping the project accessible for newcomers.
