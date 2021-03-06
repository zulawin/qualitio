from django.conf.urls.defaults import *

from qualitio.execute.views import *

urlpatterns = patterns('',
                       url(r'^$', index),

                       url(r'^ajax/get_children$', get_children),
                       url(r'^ajax/testrundirectory/(?P<directory_id>\d+)/details/?$', directory_details),
                       url(r'^ajax/testrundirectory/(?P<directory_id>\d+)/new/?$', directory_new),
                       url(r'^ajax/testrundirectory/(?P<directory_id>\d+)/edit/?$', directory_edit),

                       url(r'^ajax/testrun/(?P<testrun_id>\d+)/details/?$', testrun_details),
                       url(r'^ajax/testrun/(?P<testrun_id>\d+)/notes/?$', testrun_notes),
                       url(r'^ajax/testrun/(?P<testrun_id>\d+)/edit/?$', testrun_edit),
                       url(r'^ajax/testrun/(?P<testrun_id>\d+)/execute/?$',testrun_execute),

                       # url(r'filter/?$', filter)
                       )
