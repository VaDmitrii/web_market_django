from django.db import models


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


class User(models.Model):
    ROLES = [
        ('member', 'пользователь'),
        ('moderator', 'модератор'),
        ('admin', 'администратор'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30, choices=ROLES, null=True)
    age = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
