# Generated by Django 4.2.1 on 2023-05-23 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_alter_jobcreatemodel_nature"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobcreatemodel",
            name="qualifications",
            field=models.TextField(default="Not specified"),
            preserve_default=False,
        ),
    ]
