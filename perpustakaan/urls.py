from django.conf.urls.defaults import patterns, include, url
from perpustakaan.models import *
from django.views.generic import DetailView, ListView

urlpatterns = patterns('perpustakaan.views',

  url(r'^admin/library/loan/$', 'lateLoans'),

  url(r'^$', 'booksBy'),
  url(r'^bk$', 'booksBy'),

  url(r'^bk/(?P<pk>\d+)/$', 'book'),

  url(r'^bk/(?P<args>.+)/$', 'booksBy'),
)
