# Generated by Django 5.0 on 2023-12-15 06:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("first_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="album",
            old_name="release_data",
            new_name="release_date",
        ),
    ]
