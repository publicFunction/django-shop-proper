from django import template

from categories.views import createMenu

register = template.Library()

@register.inclusion_tag('category/cat_menu.html', takes_context=True)
def category_menu(context):
    return {'menu_list' : createMenu()}