from django import template

register = template.Library()

@register.filter
def filter(tasks, query):
    key, value = query.split(':')
    return tasks.filter(**{key: value})