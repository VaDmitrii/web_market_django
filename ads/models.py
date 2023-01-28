from django.db import models

from category.models import Category
from users.models import User


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    is_published = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name

    @property
    def username(self):
        user = User.objects.get(pk=self.author_id.id)
        return user.username
