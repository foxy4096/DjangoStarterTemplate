# Generated by Django 4.2.4 on 2023-09-07 03:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_accountinterfaces"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AccountInterfaces",
        ),
    ]
