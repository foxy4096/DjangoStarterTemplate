# Generated by Django 4.2.3 on 2023-10-13 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("analytics", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="objectviewed",
            name="content_type",
            field=models.ForeignKey(
                help_text="Content type",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="objectviewed",
            name="ip_address",
            field=models.CharField(
                blank=True,
                help_text="IP address of the user",
                max_length=120,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="objectviewed",
            name="object_id",
            field=models.PositiveIntegerField(help_text="Content type object id"),
        ),
        migrations.AlterField(
            model_name="objectviewed",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, help_text="Date and time when the object was viewed"
            ),
        ),
        migrations.AlterField(
            model_name="objectviewed",
            name="user",
            field=models.ForeignKey(
                blank=True,
                help_text="User that viewed the object",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="UserSession",
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
                    "session_key",
                    models.CharField(
                        blank=True, help_text="Session key", max_length=40, null=True
                    ),
                ),
                (
                    "is_session_active",
                    models.BooleanField(
                        default=True, help_text="Is the session active?"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the session",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Server date and time when the item was created modified",
                        verbose_name="Date created",
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Server date and time when the item was last modified",
                        verbose_name="Date modified",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        help_text="User that the session is associated with",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PageViewed",
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
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the session",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Server date and time when the item was created modified",
                        verbose_name="Date created",
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Server date and time when the item was last modified",
                        verbose_name="Date modified",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        help_text="The user that viewed the page",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_session",
                    models.ForeignKey(
                        blank=True,
                        help_text="The user session that the page was viewed in",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="analytics.usersession",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="objectviewed",
            name="user_session",
            field=models.ForeignKey(
                blank=True,
                help_text="User session that the object was viewed in",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="analytics.usersession",
            ),
        ),
    ]
