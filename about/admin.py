from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """Admin view for :model:`about.About`.

    Provides rich text editing via Summernote for the content field.
    """

    summernote_fields = ("content",)


# Register your models here.
# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """Admin view for :model:`about.CollaborateRequest`.

    Displays the message and read status in the admin list view.
    """

    list_display = (
        "message",
        "read",
    )
