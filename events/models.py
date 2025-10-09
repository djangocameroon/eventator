from django.db import models
from django.contrib.auth.models import User


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

    @property
    def vote_count(self):
        """Return the total number of votes for this event."""
        return self.votes.count()

    @property
    def is_liked_by_user(self, user):
        """Check if a specific user has voted for this event."""
        if not user or not user.is_authenticated:
            return False
        return self.votes.filter(user=user).exists()


class Vote(models.Model):
    """Represents a user's vote on an event."""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_votes')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='votes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'event']
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return f"{self.user.username} voted for {self.event.title}"
