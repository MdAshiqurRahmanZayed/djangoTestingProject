# Generated by Django 4.1.2 on 2022-10-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_blog_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(blank=True, default=1, upload_to="images/"),
            preserve_default=False,
        ),
    ]
