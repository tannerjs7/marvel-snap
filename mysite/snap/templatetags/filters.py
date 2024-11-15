from django import template


register = template.Library()


@register.filter
def lookup(d, key):
    return d[key]


@register.filter
def lookup0(d, key):
    return d[key][0]


@register.filter
def lookup1(d, key):
    return d[key][1]