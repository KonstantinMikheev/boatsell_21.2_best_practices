# Generated by Django 5.1 on 2024-09-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Почта'),
        ),
    ]
