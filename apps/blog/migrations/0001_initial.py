# Generated by Django 4.2.4 on 2023-10-16 19:04

import apps.blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                    "date_deleted",
                    models.DateTimeField(
                        blank=True,
                        help_text="Server date and time when the item was deleted",
                        null=True,
                        verbose_name="Date deleted",
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="The title of the post", max_length=200),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        help_text="The URL slug based on the post title, slug fields should be 50 characters or                            less",
                        max_length=200,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "release_status",
                    models.CharField(
                        choices=[
                            ("draft", "Draft"),
                            ("review", "Review"),
                            ("published", "Published"),
                            ("archived", "Archived"),
                        ],
                        default="draft",
                        help_text="Current status of the post",
                        max_length=55,
                        verbose_name="Release status",
                    ),
                ),
                (
                    "content",
                    django_ckeditor_5.fields.CKEditor5Field(
                        help_text="Primary content of the post using rich text editor",
                        verbose_name="Content",
                    ),
                ),
                (
                    "featured_image_raw",
                    models.ImageField(
                        blank=True,
                        help_text="Original unedited image of the post",
                        null=True,
                        upload_to=apps.blog.models.upload_to_featured_images,
                    ),
                ),
                (
                    "featured_image",
                    models.ImageField(
                        blank=True,
                        help_text="Featured image of the post",
                        null=True,
                        upload_to=apps.blog.models.upload_to_featured_images,
                    ),
                ),
                (
                    "featured_image_thumbnail",
                    models.ImageField(
                        blank=True,
                        help_text="Featured image thumbnail of the post",
                        null=True,
                        upload_to=apps.blog.models.upload_to_featured_images,
                    ),
                ),
                (
                    "meta_title",
                    models.CharField(
                        blank=True,
                        help_text="Title that will appear in search engines and browser tab. Recommended                                  length is 50-60 characters",
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "meta_description",
                    models.CharField(
                        blank=True,
                        help_text="Summary of the post. Recommended length is 50-160 characters",
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "meta_keywords",
                    models.CharField(
                        blank=True,
                        help_text="Comma-separated keywords. Keywords that describe the post. Recommended                                     number of keywords is 3-8",
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "allow_comments",
                    models.BooleanField(
                        default=True,
                        help_text="If checked, comments are allowed for this post",
                        verbose_name="Allow comments",
                    ),
                ),
                (
                    "allow_sharing",
                    models.BooleanField(
                        default=True,
                        help_text="If checked, social media sharing is allowed for this post",
                        verbose_name="Allow social media sharing",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the post",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="If checked, the post is deleted",
                        verbose_name="Is deleted",
                    ),
                ),
                (
                    "date_published",
                    models.DateTimeField(
                        blank=True,
                        help_text="Server date and time when the item was published",
                        null=True,
                        verbose_name="Date published",
                    ),
                ),
                (
                    "authors",
                    models.ManyToManyField(
                        help_text="Post authors.",
                        related_name="authored_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="User who created the post",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "deleted_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who deleted the post",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="deleted_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "lead_author",
                    models.ForeignKey(
                        help_text="Lead author of the post",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="authored_posts_as_lead",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        help_text="User who last modified the post",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="modified_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                    "date_deleted",
                    models.DateTimeField(
                        blank=True,
                        help_text="Server date and time when the item was deleted",
                        null=True,
                        verbose_name="Date deleted",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        help_text="Comment content",
                        max_length=6000,
                        verbose_name="Content",
                    ),
                ),
                (
                    "is_flagged",
                    models.BooleanField(
                        default=False,
                        help_text="Has the comment been flagged as a potential problem?",
                        verbose_name="Is flagged",
                    ),
                ),
                (
                    "is_edited",
                    models.BooleanField(
                        default=False,
                        help_text="Has the comment been edited by the user?",
                        verbose_name="Is edited",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="Has the comment been deleted by the user?",
                        verbose_name="Is deleted",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the item",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "downvotes",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Users who have downvoted this comment",
                        related_name="comment_downvotes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent_comment",
                    models.ForeignKey(
                        blank=True,
                        help_text="The parent comment that this comment replied to",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="child_comments",
                        to="blog.comment",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        help_text="The post that the comment is related to",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_comment",
                        to="blog.post",
                    ),
                ),
                (
                    "upvotes",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Users who have upvoted this comment",
                        related_name="comment_upvotes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User that made the comment",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_comment",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
