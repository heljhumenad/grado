from django import template

register = template.Library()


@register.filter
def check_teacher(id=None):
    pass
