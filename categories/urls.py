from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('categories.views',

    url(r'^$', 'get_categories', name='get_categories'),
    url(r'^(?P<category>[-\w]+)/$', 'view_category', name='view_category'),
    url(r'^(?P<category>[-\w]+)/(?P<sub_category>[-\w]+)/', 'view_product_list', name='view_product_list'),
    
)