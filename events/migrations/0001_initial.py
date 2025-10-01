from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "event_date",
                    models.DateField(
                        help_text="Date the event is scheduled to take place."
                    ),
                ),
                ("location", models.CharField(max_length=255)),
                (
                    "organizer",
                    models.CharField(
                        default="Django Cameroon",
                        help_text="Defaults to Django Cameroon but can be overridden for partner events.",
                        max_length=255,
                    ),
                ),
                ("registration_url", models.URLField(blank=True)),
                (
                    "is_published",
                    models.BooleanField(
                        default=False,
                        help_text="Unpublished items are treated as ideas awaiting review.",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["event_date", "title"],
            },
        ),
    ]
