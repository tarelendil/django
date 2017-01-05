from django import template
register=template.Library()

@register.filter(name='lookup')

def get_value_from_dict(dict, key):
    if key:
        return dict.get(key)