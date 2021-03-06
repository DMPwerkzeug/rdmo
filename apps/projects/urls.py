from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import *

urlpatterns = [
    url(r'^$', projects, name='projects'),
    url(r'^(?P<pk>[0-9]+)/$', project, name='project'),

    url(_(r'^create/$'), ProjectCreateView.as_view(), name='project_create'),
    url(_(r'^(?P<pk>[0-9]+)/update/$'), ProjectUpdateView.as_view(), name='project_update'),
    url(_(r'^(?P<pk>[0-9]+)/delete/$'), ProjectDeleteView.as_view(), name='project_delete'),

    url(_(r'^(?P<pk>[0-9]+)/summary/$'), project_summary, name='project_summary'),

    url(_(r'^(?P<project_id>[0-9]+)/questions/'), project_questions, name='project_questions'),
]
