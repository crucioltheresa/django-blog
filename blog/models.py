from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    """Stores a single blog post entry, related to :model:`auth.User`.

    **Fields**
    ``title``
        The title of the post (max 200 characters, unique).
    ``slug``
        URL-friendly identifier for the post (max 200 characters, unique).
    ``author``
        A foreign key to :model:`auth.User`.
    ``featured_image``
        A Cloudinary image field for the post's featured image.
    ``content``
        The main body text of the post.
    ``created_on``
        The date and time the post was created.
    ``status``
        Publication status: 0 for Draft, 1 for Published.
    ``excerpt``
        A short summary of the post.
    ``updated_on``
        The date and time the post was last updated.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField("image", default="placeholder")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """Return a string representation of the post.

        **Returns**
            A string with the post title and author name.
        """
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """Stores a single comment entry, related to :model:`blog.Post`
    and :model:`auth.User`.

    **Fields**
    ``post``
        A foreign key to :model:`blog.Post`.
    ``author``
        A foreign key to :model:`auth.User`.
    ``body``
        The text content of the comment.
    ``approved``
        Boolean indicating if the comment has been approved by an admin.
    ``created_on``
        The date and time the comment was created.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """Return a string representation of the comment.

        **Returns**
            A string with the comment body and author name.
        """
        return f"Comment {self.body} by {self.author}"
