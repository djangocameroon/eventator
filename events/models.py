from django.db import models


class Event(models.Model):
    """Represents a Hacktoberfest community event or idea."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField(
        help_text="Date the event is scheduled to take place."
    )
    location = models.CharField(max_length=255)
    organizer = models.CharField(
        max_length=255,
        default="Django Cameroon",
        help_text="Defaults to Django Cameroon but can be overridden for partner events.",
    )
    registration_url = models.URLField(blank=True)
    is_published = models.BooleanField(
        default=False,
        help_text="Unpublished items are treated as ideas awaiting review.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["event_date", "title"]

    def __str__(self) -> str:
        return f"{self.title} ({self.event_date})"
