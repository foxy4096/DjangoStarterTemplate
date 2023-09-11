# Generated by Django 4.2.4 on 2023-09-11 01:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                (
                    "name",
                    models.CharField(help_text="Name of the country", max_length=255),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        help_text="The slug based on the country name",
                        max_length=255,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "country_code",
                    models.CharField(
                        help_text="Code of the country (e.g., US, UK, etc.)",
                        max_length=255,
                    ),
                ),
                (
                    "phone_code",
                    models.IntegerField(
                        help_text="Phone code of the country (e.g., 1, 44, etc.)"
                    ),
                ),
                (
                    "flag",
                    models.ImageField(
                        help_text="Flag of the country", upload_to="flags"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the country",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Server date and time when the country was created",
                        verbose_name="Date created",
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Server date and time when country was last modified",
                        verbose_name="Date modified",
                    ),
                ),
            ],
        ),
    ]
