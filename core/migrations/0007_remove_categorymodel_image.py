# Generated by Django 4.2.1 on 2023-05-22 08:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_remove_categorymodel_description_categorymodel_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="categorymodel",
            name="image",
        ),
    ]
