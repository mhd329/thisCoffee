from django.db import models
from django.contrib.auth import validators
from config.settings import AUTH_USER_MODEL
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(AbstractBaseUser):
    profileimage = ProcessedImageField(
        upload_to="static/images/userProfileImages/",
        blank=True,
        format="JPEG",
        options={"quality": 60},
    )
    username = models.CharField(
        error_messages={"unique": "A user with that username already exists."},
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        max_length=150,
        unique=True,
        validators=[validators.UnicodeUsernameValidator()],
        verbose_name="아이디",
    )
    nickname = models.CharField(
        max_length=20,
        verbose_name="닉네임",
    )
    email = models.EmailField(
        blank=True,
        max_length=100,
        verbose_name="이메일",
    )
    stamp = models.IntegerField(
        default=0,
        verbose_name="출석",
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name="가입일",
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name="관리자 여부",
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = "User"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nickname"]
