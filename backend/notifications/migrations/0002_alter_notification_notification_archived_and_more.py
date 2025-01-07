# Generated by Django 4.2.4 on 2025-01-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_priority',
            field=models.IntegerField(default=False),
        ),
    ]
