# Generated by Django 4.2.4 on 2025-01-03 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('task_description', models.TextField()),
                ('task_due_date', models.DateTimeField()),
                ('task_priority', models.CharField(max_length=255)),
                ('task_status', models.CharField(max_length=255)),
                ('task_comments', models.TextField()),
                ('task_assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('task_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
