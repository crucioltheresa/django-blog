from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
class PostList(generic.ListView):
    """Display a paginated list of all :model:`blog.Post` entries.

    **Context**
    ``post_list``
        A queryset of all :model:`blog.Post` instances.
    **Template**
        :template:`blog/index.html`
    """

    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """Display an individual :model:`blog.Post`

    **Context**
    ``post``
        An instance of :model:`blog.Post`
    **Template**
        :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval."
            )

    comment_form = CommentForm()
    print("About to render template")

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "coder": "Maria Theresa Cruciol",
        },
    )


def comment_edit(request, slug, comment_id):
    """Edit an individual comment on a :model:`blog.Post`.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        An instance of :model:`blog.Comment` to be edited.
    ``comment_form``
        An instance of :form:`blog.CommentForm` pre-populated with the comment data.
    **Returns**
        Redirects to :template:`blog/post_detail.html`.
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """Delete an individual comment on a :model:`blog.Post`.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        An instance of :model:`blog.Comment` to be deleted.
    **Returns**
        Redirects to :template:`blog/post_detail.html`.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(
        queryset, slug=slug
    )  # Ensure the post exists and is published
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))
