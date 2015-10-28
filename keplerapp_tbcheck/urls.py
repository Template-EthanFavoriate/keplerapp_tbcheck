from django.conf.urls import patterns, url

print 'sub url called'

urlpatterns = patterns('',
    url(r'dict', 'keplerapp_tbcheck.views.service_check'),
    url(r'', 'keplerapp_tbcheck.views.service_default')
)
