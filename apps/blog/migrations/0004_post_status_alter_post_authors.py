# Generated by Django 4.2.2 on 2023-06-29 00:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_post_date_created_post_date_modified_post_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('in_draft', 'In draft'), ('in_review', 'In review'), ('published', 'Published')], default='in_draft', help_text='Current status of the post', max_length=55, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=models.ManyToManyField(help_text='Post authors.', related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
