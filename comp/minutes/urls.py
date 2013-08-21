from django.conf.urls import patterns, url

urlpatterns = patterns('minutes.views',
        url(r'^$', 'index'), # /minutes/
        url(r'^(?P<pk>\d+)/$', 'detail', name='minutes'), # /minutes/3
)
