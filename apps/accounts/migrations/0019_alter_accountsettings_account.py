# Generated by Django 4.2.3 on 2023-10-10 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0018_remove_account_date_deleted_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountsettings",
            name="account",
            field=models.OneToOneField(
                help_text="Account that is connected to the settings",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="settings",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Account",
            ),
        ),
    ]