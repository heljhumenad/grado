from django import template

register = template.Library()


@register
def check_teacher(id=None):
    pass
