from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """A form for submitting a collaboration request via :model:`about.CollaborateRequest`.

    Collects the requester's ``name``, ``email`` address, and ``message``.
    """

    class Meta:
        model = CollaborateRequest
        fields = (
            "name",
            "email",
            "message",
        )
