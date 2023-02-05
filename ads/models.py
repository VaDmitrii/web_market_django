from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from users.models import User


def status_false(value: str):
    if value is True:
        raise ValidationError("Ad publishing status should be false")


class Category(models.Model):
    CHOICES = [
        ("cats", "Котики"),
        ("dogs", "Песики"),
        ("books", "Книги"),
        ("plants", "Растения"),
        ("furniture&design", "Мебель и интерьер")
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, choices=CHOICES, null=True)
    slug = models.CharField(max_length=10, unique=True, null=True, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=2000, blank=True, null=True)
    is_published = models.BooleanField(max_length=20, validators=[status_false], default=False)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name

    @property
    def username(self):
        user = User.objects.get(pk=self.author.id)
        return user.username


class Selection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
