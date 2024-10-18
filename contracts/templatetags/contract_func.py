from django import template

register = template.Library()

@register.simple_tag
def short_obj(obj):
    if len(obj) > 25:
        return f'{obj[:25]}...'
    return obj
