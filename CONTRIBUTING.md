# Contributor Guide

Thank you for helping improve Eventator. This guide outlines the local workflow and a few expectations so that contributions stay consistent.

## Environment setup
1. Install Python 3.10 or later.
2. Install [uv](https://github.com/astral-sh/uv).
3. Install project dependencies:
   ```bash
   uv sync
   ```

## Running Django commands
Use `uv run` to execute all Django commands through the managed environment:
- Apply migrations: `uv run python manage.py migrate`
- Load sample data: `uv run python manage.py seed_events`
- Start the server: `uv run python manage.py runserver`
- Run tests: `uv run python manage.py test`

## Coding standards
- Keep the project free of unused comments and stray debug prints.
- Follow Django best practices and prefer clarity over clever solutions.
- Ensure templates remain compatible with Tailwind CDN usage; no build step should be required.
- Maintain database-agnostic code even though SQLite is the default.

## Adding data
Seed data is stored in `data/events.json`. Update this file if you want to supply new default events. Always verify that JSON entries include at minimum `title` and an ISO-formatted `event_date`.

## Submitting changes
1. Leave a star ⭐
2. Create a feature branch.
3. Run the test suite (`uv run python manage.py test`).
4. Document user-facing changes in `README.md` when relevant.
5. Open a pull request describing the motivation, the approach taken, and any follow-up work.

By keeping these steps in mind we can provide a smooth onboarding experience for contributors joining Hacktoberfest 2025 with Django Cameroon.
