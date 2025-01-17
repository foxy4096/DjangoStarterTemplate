from django import template
from django.db import models

register = template.Library()


@register.filter(name='verbose_name')
def verbose_name(instance, field_name):
    """
    Returns verbose name for a field.
    """
    return instance._meta.get_field(field_name).verbose_name.title()


@register.filter(name='field_value')
def field_value(instance, field_name):
    """
    Returns the value for a specific field from a Django model instance.

    Args:
        instance: Django model instance.
        field_name: String name of the model field.

    Returns:
        Value of the specified field or None if field doesn't exist.
    """
    # Check if instance is a Django model instance
    if not isinstance(instance, models.Model):
        return None

    # Return the field's value or None if it doesn't exist
    return getattr(instance, field_name, None)


@register.filter(name='pluralize', is_safe=True)
def pluralize(value, arg='s'):
    if value != 1:
        return arg
    return ''
