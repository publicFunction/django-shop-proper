from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns

from products.views import view_products_list

urlpatterns = patterns('products.views',

    url(r'^(?P<category>[-\w]+)/(?P<sub_category>[-w]+)/$', 'view_products_list', name='view_products_list'),
    
)