from django import template

register = template.Library()

@register.filter()
def media_filtr(path):
    if path:
        return f"media/{path}"
    return "#"

