from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('theshop.views',
    url(r'^', 'index', name='shop_index'),
    
)