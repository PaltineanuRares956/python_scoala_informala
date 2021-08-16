from django import template

register = template.Library()


@register.filter
@register.inclusion_tag('products-list.html')
def quantity_converter(value, arg):
    return value*int(arg)/100
