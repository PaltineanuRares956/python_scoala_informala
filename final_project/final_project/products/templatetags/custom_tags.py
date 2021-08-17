from django import template

register = template.Library()


@register.filter
def quantity_converter(value, arg):
    return value*arg/100
