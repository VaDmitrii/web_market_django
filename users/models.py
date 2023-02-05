from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

def age_min(value: date):
    if date.today().year - value.year < 9:
        raise ValidationError(
            "User must be at least 9 years old"
        )


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    lat = models.DecimalField(max_digits=15, decimal_places=6)
    lng = models.DecimalField(max_digits=15, decimal_places=6)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLES = [
        ('member', 'пользователь'),
        ('moderator', 'модератор'),
        ('admin', 'администратор'),
    ]

    role = models.CharField(max_length=30, choices=ROLES, null=True)
    age = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField(null=True, validators=[age_min])

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
