# Generated by Django 4.2.4 on 2025-01-03 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='uploaded_at',
        ),
    ]
