from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import EventIdeaForm
from .models import Event


def home(request):
    """Landing page listing published events and collecting new ideas."""

    published_events = Event.objects.filter(is_published=True)
    pending_ideas = Event.objects.filter(is_published=False)

    if request.method == "POST":
        form = EventIdeaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks for sharing your idea! We will review it and publish it once approved.",
            )
            return redirect(reverse("events:home"))
    else:
        form = EventIdeaForm()

    context = {
        "events": published_events,
        "pending_count": pending_ideas.count(),
        "form": form,
    }
    return render(request, "events/home.html", context)


def submissions(request):
    """Page showing all submitted content with review status."""

    all_events = Event.objects.all().order_by("-created_at")

    context = {
        "submissions": all_events,
    }
    return render(request, "events/submissions.html", context)
