from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def chunk_list(value, chunk_size):
    """Divise une liste en sous-listes de taille chunk_size."""
    if not isinstance(value, list):
        return value
    return [value[i:i + chunk_size] for i in range(0, len(value), chunk_size)]