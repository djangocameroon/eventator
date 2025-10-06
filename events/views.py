from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import EventIdeaForm
from .models import Event, Vote


def home(request):
    """Landing page listing published events and collecting new ideas."""

    published_events = Event.objects.filter(is_published=True).prefetch_related('votes')
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

    all_events = Event.objects.all().prefetch_related('votes').order_by("-created_at")

    context = {
        "submissions": all_events,
    }
    return render(request, "events/submissions.html", context)


@login_required
@require_POST
def vote_event(request, event_id):
    """Toggle vote for an event."""
    event = get_object_or_404(Event, id=event_id)
    
    # Check if user already voted
    vote, created = Vote.objects.get_or_create(
        user=request.user,
        event=event
    )
    
    if not created:
        # User already voted, remove the vote
        vote.delete()
        voted = False
    else:
        # User just voted
        voted = True
    
    # Return JSON response for AJAX
    return JsonResponse({
        'voted': voted,
        'vote_count': event.vote_count,
        'event_id': event.id
    })
