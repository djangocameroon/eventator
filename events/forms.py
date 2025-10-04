from django import forms

from .models import Event


class EventIdeaForm(forms.ModelForm):
    """Form for community members to suggest new event ideas."""

    event_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        help_text="Pick the tentative date for your idea.",
    )

    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "event_date",
            "location",
            "organizer",
            "registration_url",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault(
                "class",
                "w-full rounded-xl border border-indigo-200/20 bg-slate-900/60 px-4 py-3 text-sm text-white placeholder-slate-400 focus:border-indigo-400 focus:outline-none focus:ring-2 focus:ring-indigo-400/50",
            )
            field.widget.attrs.setdefault("placeholder", field.label)

    def save(self, commit: bool = True) -> Event:
        instance: Event = super().save(commit=False)
        instance.is_published = False
        if commit:
            instance.save()
            self.save_m2m()
        return instance
