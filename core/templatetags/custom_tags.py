from django import template

register = template.Library()

@register.filter(name="add_pound_sign")
def add_pound_sign(value):
    return f'£{value}'