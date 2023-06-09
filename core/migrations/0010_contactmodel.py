# Generated by Django 4.2.1 on 2023-05-25 02:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_jobcreatemodel_qualifications"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactModel",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("subject", models.CharField(max_length=255)),
                ("message", models.CharField(max_length=255)),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
