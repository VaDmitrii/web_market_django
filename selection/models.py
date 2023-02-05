# from django.db import models
#
# from ads.models import Ad
# from users.models import User
#
#
# class Selection(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     items = models.ManyToManyField(Ad)
#
#     class Meta:
#         verbose_name = "Подборка"
#         verbose_name_plural = "Подборки"
#
#     def __str__(self):
#         return self.name
