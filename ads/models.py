from django.db import models


class Category(models.Model):
    CHOICES = [
        ("cats", "Котики"),
        ("dogs", "Песики"),
        ("books", "Книги"),
        ("plants", "Растения"),
        ("furniture&design", "Мебель и интерьер")
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=18, choices=CHOICES, null=True)

    def __str__(self):
        return self.name


class Ad(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=5)
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=200)
    is_published = models.CharField(max_length=20)

    def __str__(self):
        return self.name
