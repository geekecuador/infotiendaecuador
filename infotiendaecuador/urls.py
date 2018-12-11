"""infotiendaecuador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from infotienda.views import index, busqueda, single, Locales, subscribe,privacidad,agregar,ingresarlocal
from infotiendaecuador import settings

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    path('', index),
    path('busqueda/', busqueda.as_view()),
    path('local/', single),
    path('privacidad/', privacidad),
    path('agregar/', agregar),
    path('locales/<slug:slug>/', Locales.as_view(), name='locales'),
    path('subscribe/', subscribe, name="subscribe"),
    path('ingresarlocal/',ingresarlocal,name="ingresarlocal")
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = 'InfoTiendaEcuador'
