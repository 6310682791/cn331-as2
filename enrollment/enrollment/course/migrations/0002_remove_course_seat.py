# Generated by Django 4.1 on 2022-09-12 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='seat',
        ),
    ]
