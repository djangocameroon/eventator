from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.home, name="home"),
    path("submissions/", views.submissions, name="submissions"),
    path("vote/<int:event_id>/", views.vote_event, name="vote_event"),
]
