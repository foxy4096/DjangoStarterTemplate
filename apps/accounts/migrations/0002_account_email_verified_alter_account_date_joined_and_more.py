# Generated by Django 4.2.2 on 2023-06-16 18:21

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email_verified',
            field=models.BooleanField(default=False, help_text='Designates whether the user has verified their email address', verbose_name='Email verified'),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, help_text='Server date and time the account was created', verbose_name='Date joined'),
        ),
        migrations.AlterField(
            model_name='account',
            name='description',
            field=models.TextField(blank=True, help_text='User bio or description', max_length=2000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(help_text='Unique email address', max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, help_text='First name', max_length=120, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site', verbose_name='Admin status'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_profile_public',
            field=models.BooleanField(default=True, help_text='Designates whether the user profile can be viewed by others', verbose_name='Profile public'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site', verbose_name='Staff status'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them', verbose_name='Superuser status'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now=True, help_text='Server date and time the account last logged in', verbose_name='Last login'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, help_text='Last name', max_length=120, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, help_text='Profile image or avatar', null=True, upload_to='profile_images/', verbose_name='Profile image'),
        ),
        migrations.AlterField(
            model_name='account',
            name='short_uuid',
            field=models.CharField(editable=False, help_text='Short unique identifier for the account', max_length=8, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=8, message='Short UUID must be exactly 8 characters long')], verbose_name='Short UUID'),
        ),
        migrations.AlterField(
            model_name='account',
            name='theme',
            field=models.CharField(choices=[('light', 'Light'), ('dark', 'Dark'), ('system', 'System')], default='system', help_text='User website theme', max_length=55, verbose_name='Theme'),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(help_text='Unique username associated with the account', max_length=16, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be alphanumeric or contain any of the following: "_"', regex='^[a-zA-Z0-9_]*$'), django.core.validators.MinLengthValidator(limit_value=4, message='Username must be at least 4 characters long')], verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='account',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for the account', unique=True, verbose_name='UUID'),
        ),
    ]
