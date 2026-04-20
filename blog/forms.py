from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """A form for creating and editing a :model:`blog.Comment`.

    Allows users to submit comment text via the ``body`` field.
    """

    class Meta:
        model = Comment
        fields = ("body",)
