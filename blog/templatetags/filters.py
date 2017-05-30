from django import template


register = template.Library()

@register.filter(name='get_text_excerpt')
def get_text_excerpt(value):
    start = value.index('<p>')


    return value[start+3:start+45]

@register.filter(name = 'modulo')
def modulo(num, val):
    return num % val