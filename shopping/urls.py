from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                        url(r'^category/', include('categories.urls')),
                        url(r'^', include('theshop.urls')),
)

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns