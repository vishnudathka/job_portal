# Generated by Django 4.2.1 on 2023-05-21 12:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoryModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="JobCreateModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("jobtitle", models.CharField(max_length=255)),
                ("jobdescription", models.TextField()),
                (
                    "nature",
                    models.CharField(
                        choices=[
                            ("full_time", "Full Time"),
                            ("part_time", "Part Time"),
                            ("contract", "Contract"),
                            ("freelance", "Freelance"),
                            ("internship", "Internship"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "salary",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("company", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("requirements", models.TextField()),
                ("deadline", models.DateTimeField()),
                ("company_description", models.TextField()),
                ("company_website", models.URLField()),
                ("responsibilities", models.TextField()),
                ("image", models.ImageField(upload_to="job_images")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.categorymodel",
                    ),
                ),
                ("skills", models.ManyToManyField(to="core.skill")),
            ],
        ),
    ]