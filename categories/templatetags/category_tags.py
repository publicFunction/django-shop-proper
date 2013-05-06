from django import template
from itertools import chain
from categories.models import Category

register = template.Library()

@register.inclusion_tag('category/cat_menu.html', takes_context=True)
def category_menu(context):
    
    return {'nodes' : Category.objects.filter(published=True)}