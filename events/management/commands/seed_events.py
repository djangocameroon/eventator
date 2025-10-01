import json
from datetime import date
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from events.models import Event


class Command(BaseCommand):
    help = "Seed the database with Hacktoberfest events from a JSON file."

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            help="Optional custom path to the JSON seed file. Defaults to data/events.json",
        )
        parser.add_argument(
            "--draft",
            action="store_true",
            help="Flag seeded events as ideas awaiting approval instead of publishing them.",
        )

    def handle(self, *args, **options):
        seed_path = options.get("path")
        as_draft = options.get("draft", False)

        default_path = Path("data") / "events.json"
        path = Path(seed_path) if seed_path else default_path

        if not path.exists():
            raise CommandError(f"Cannot find seed file at {path.resolve()}")

        self.stdout.write(self.style.NOTICE(f"Loading events from {path.resolve()}"))

        with path.open() as handle:
            try:
                payload = json.load(handle)
            except json.JSONDecodeError as exc:
                raise CommandError(f"Invalid JSON: {exc}") from exc

        if not isinstance(payload, list):
            raise CommandError("Seed file must contain a list of event objects")

        created, updated = 0, 0
        with transaction.atomic():
            for entry in payload:
                try:
                    title = entry["title"]
                    event_date_str = entry["event_date"]
                except KeyError as exc:
                    raise CommandError(f"Missing required key: {exc}") from exc

                try:
                    event_date = date.fromisoformat(event_date_str)
                except ValueError as exc:
                    raise CommandError(
                        f"Invalid date '{event_date_str}' for event '{title}'. Expected ISO format YYYY-MM-DD."
                    ) from exc

                defaults = {
                    "description": entry.get("description", ""),
                    "location": entry.get("location", "To be announced"),
                    "organizer": entry.get("organizer", "Django Cameroon"),
                    "registration_url": entry.get("registration_url", ""),
                    "is_published": not as_draft,
                }

                obj, created_flag = Event.objects.update_or_create(
                    title=title,
                    event_date=event_date,
                    defaults=defaults,
                )
                action = "Created" if created_flag else "Updated"
                self.stdout.write(
                    f'{action} "{obj.title}" scheduled for {obj.event_date}'
                )
                if created_flag:
                    created += 1
                else:
                    updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed complete. Created {created} event(s) and updated {updated} event(s).",
            )
        )
