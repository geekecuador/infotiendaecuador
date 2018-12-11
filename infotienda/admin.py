from django.contrib import admin
from django.contrib.gis.db import models
from solo.admin import SingletonModelAdmin

from .models import Local, Canton, Provincia, Categorias, Subcategorias, ImagenLocal, ConfiguracioSitio, Subscribe

# Register your models here.

admin.site.register(Canton)
admin.site.register(Provincia)

admin.site.register(ConfiguracioSitio, SingletonModelAdmin)
admin.site.register(Categorias)
admin.site.register(Subscribe)
admin.site.register(Subcategorias)

from mapwidgets.widgets import GoogleStaticMapWidget


class PropertyImageInline(admin.TabularInline):
    model = ImagenLocal
    extra = 1


class LocalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GoogleStaticMapWidget}
    }
    inlines = [PropertyImageInline, ]


admin.site.register(Local, LocalAdmin)
