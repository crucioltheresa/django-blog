from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Admin view for :model:`blog.Post`.

    Provides rich text editing via Summernote for the content field,
    with list display, search, and filter options.
    """

    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


# Register your models here.
admin.site.register(Comment)
