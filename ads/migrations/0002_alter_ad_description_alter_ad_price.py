# Generated by Django 4.1.5 on 2023-01-29 13:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]