from django.db import models
from config.settings import AUTH_USER_MODEL
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    profileimage = ProcessedImageField(
        upload_to="static/images/userProfileImages/",
        blank=True,
        format="JPEG",
        options={"quality": 60},
    )
    