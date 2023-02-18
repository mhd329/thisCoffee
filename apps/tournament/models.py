from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CoffeeType(models.Model):
    origin = models.CharField(max_length=10)
    characteristic = models.TextField()
    # 1 약함
    # 2 중간
    # 3 강함
    flavor = models.IntegerField(
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1),
        ],
    )
    acidity = models.IntegerField(
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1),
        ],
    )
    bitter = models.IntegerField(
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1),
        ],
    )
    body = models.IntegerField(
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1),
        ],
    )

    class Meta:
        db_table = "CoffeeType"
