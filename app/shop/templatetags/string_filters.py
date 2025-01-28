from django import template

register = template.Library()

@register.filter
def split(value, delimiter=' '):
    """Разделяет строку по указанному разделителю."""
    if not value:
        return []
    return value.split(delimiter)
