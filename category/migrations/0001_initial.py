# Generated by Django 4.1.4 on 2023-01-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('cats', 'Котики'), ('dogs', 'Песики'), ('books', 'Книги'), ('plants', 'Растения'), ('furniture&design', 'Мебель и интерьер')], max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
