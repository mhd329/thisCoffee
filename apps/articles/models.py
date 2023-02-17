from django.db import models
from config.settings import AUTH_USER_MODEL


# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    img = models.ImageField(
        upload_to="static/images/articleImages/",
        blank=True,
        null=True,
    )

class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name="작성자", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)