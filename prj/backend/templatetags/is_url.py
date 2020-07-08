from django import template

register = template.Library()


@register.filter(name='is_url')
def is_url(url):
    url = str(url)
    if url[:4]=="http":
        return True
    else:
        return False