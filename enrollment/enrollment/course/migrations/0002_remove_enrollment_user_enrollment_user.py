# Generated by Django 4.1.1 on 2022-10-03 11:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='user',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
