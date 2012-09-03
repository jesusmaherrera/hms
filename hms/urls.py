from django.conf.urls.defaults import *
from hms.views import index
from hms.main import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.index),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^internamientos/', views.internamientos),
    (r'^search/(.*)', views.search),
    (r'^servicios/', views.servicios),
    (r'^ubicacion/', views.ubicacion),
    (r'^derechosMedicos/', views.derechosMedicos),
    (r'^derechosPacientesAleman/', views.derechosPacientesAleman),
    (r'^derechosPacientes/', views.derechosPacientes),
    (r'^derechosEnfermeras/', views.derechosEnfermeras),
    (r'^informes/', views.informes),
    (r'^directorioMedico/', views.directorioMedico),
    #(r'^contacto/', views.nuevo_contacto),
    #url(r'^usuario/nuevo$','hms.main.views.nuevo_usuario'),
    #(r'^admin/', include('django.contrib.admin.urls')),
    # Examples:
    # url(r'^$', 'hms.views.home', name='home'),
    # url(r'^hms/', include('hms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
)

urlpatterns += staticfiles_urlpatterns()
