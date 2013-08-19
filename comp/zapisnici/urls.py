from django.conf.urls import patterns, url

urlpatterns = patterns('zapisnici.views',
        url(r'^$', 'index'), # /zapisnici/
        url(r'^(?P<pk>\d+)/$', 'detail', name='zapisnik'), # /zapisnici/3
)
