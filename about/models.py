from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class About(models.Model):
    """Stores the about page content, including a profile image.

    **Fields**
    ``title``
        The title of the about section (max 200 characters, unique).
    ``content``
        The main body text for the about page.
    ``profile_image``
        A Cloudinary image field for the profile image.
    ``updated_on``
        The date and time the content was last updated.
    """

    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    profile_image = CloudinaryField("image", default="placeholder")
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the about entry.

        **Returns**
            The title of the about entry.
        """
        return self.title


class CollaborateRequest(models.Model):
    """Stores a single collaboration request submitted via the about page.

    **Fields**
    ``name``
        The name of the person making the request (max 200 characters).
    ``email``
        The email address of the person making the request.
    ``message``
        The content of the collaboration request.
    ``read``
        Boolean indicating if the request has been read by the admin.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the collaboration request.

        **Returns**
            A string containing the requester's name.
        """
        return f"Collaboration request from {self.name}"
