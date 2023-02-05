# from django.core.validators import MinLengthValidator
# from django.db import models
#
#
# class Category(models.Model):
#     CHOICES = [
#         ("cats", "Котики"),
#         ("dogs", "Песики"),
#         ("books", "Книги"),
#         ("plants", "Растения"),
#         ("furniture&design", "Мебель и интерьер")
#     ]
#
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50, choices=CHOICES, null=True)
#     slug = models.CharField(max_length=10, unique=True, null=True, validators=[MinLengthValidator(5)])
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.name
