from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',

      url(r'^$', 'uvt.views.index'),
      url(r'^blog/', include('articles.urls')),
      url(r'^artikel/$', 'uvt.views.artikel'),
      url(r'^tutorial/$', 'uvt.views.tutorial'),
      url(r'^aplikasi/$', 'uvt.views.aplikasi'),
      url(r'^kategori/$', 'uvt.views.kategori'),
      url(r'^jadwal/$', 'uvt.views.jadwal'),
      url(r'^pastebin/', include('pastebin.urls')),
      url(r'^kontak/$', 'uvt.views.kontak'),
      url(r'^thanks/$', 'uvt.views.kontak'),
      url(r'^accounts/', include('registration.backends.default.urls')),
      url(r'^', include('perpustakaan.urls')),
      url(r'^tinymce/', include('tinymce.urls')),
      url(r'^admin/', include(admin.site.urls)),
      url(r'live/', include('live.urls')),
      url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'media'}),
      url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
      url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
      url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
    		{ 'document_root': '/home/shellc0de/uvt/uvt/uvt_edu/media/tiny_mce' }),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   )
