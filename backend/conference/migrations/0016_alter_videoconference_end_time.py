# Generated by Django 4.2.4 on 2025-01-05 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0015_alter_videoconference_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoconference',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 5, 21, 59, 5, 484611, tzinfo=datetime.timezone.utc)),
        ),
    ]
