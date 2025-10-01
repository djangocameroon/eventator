from django.test import TestCase
from django.urls import reverse

from .models import Event


class HomeViewTests(TestCase):
    def test_home_renders_events(self):
        Event.objects.create(
            title="Test Event",
            description="A simple test event.",
            event_date="2025-10-10",
            location="Yaoundé",
            is_published=True,
        )

        response = self.client.get(reverse("events:home"))
        self.assertContains(response, "Test Event")

    def test_submission_creates_unpublished_event(self):
        payload = {
            "title": "Community Sprint",
            "description": "Let's build something cool together.",
            "event_date": "2025-10-15",
            "location": "Douala",
            "organizer": "Community Member",
            "registration_url": "https://example.com",
        }
        response = self.client.post(reverse("events:home"), payload, follow=True)
        self.assertRedirects(response, reverse("events:home"))
        event = Event.objects.get(title="Community Sprint")
        self.assertFalse(event.is_published)
