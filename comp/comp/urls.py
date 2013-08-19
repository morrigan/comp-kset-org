from django.conf.urls import patterns, include, url
from utils.views import login
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^zapisnici/', include('zapisnici.urls', namespace="zapisnici")),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^$', 'flatpage', {'url': '/'}, name='comp_home'), 
    url(r'^kontakt/$', 'flatpage', {'url': '/kontakt/'}, name='comp_kontakt'), 
)
