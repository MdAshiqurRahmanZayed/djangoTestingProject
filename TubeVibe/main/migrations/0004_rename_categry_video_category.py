# Generated by Django 5.0 on 2024-01-21 04:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_video_slug_alter_video_youtube_video"),
    ]

    operations = [
        migrations.RenameField(
            model_name="video",
            old_name="categry",
            new_name="category",
        ),
    ]
