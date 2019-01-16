from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from smart_selects.db_fields import GroupedForeignKey
from solo.models import SingletonModel


class ConfiguracioSitio(SingletonModel):
    nombre_sitio = models.CharField(max_length=200)
    favicon = models.ImageField(upload_to='favicon')
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_author = models.CharField(max_length=100, blank=True)
    meta_keywords = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Configuración de sitio"
        verbose_name_plural = "Configuraciones de sitio"

    def __str__(self):
        return self.nombre_sitio



class Provincia(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"

    def __str__(self):
        return self.nombre


class Canton(models.Model):
    nombre = models.CharField(max_length=200)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cantón"
        verbose_name_plural = "Cantones"

    def __str__(self):
        return self.nombre


class Categorias(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Subcategorias(models.Model):
    nombre = models.CharField(max_length=200)
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Subcategoría"
        verbose_name_plural = "Subcategorías"

    def __str__(self):
        return self.nombre


class Local(models.Model):
    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locales"

    nombre = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    servicio = models.TextField()
    imagen = models.ImageField(upload_to='locales', null=True, blank=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, verbose_name="Categoría")
    subcategoria = GroupedForeignKey(
        Subcategorias, 'categorias', null=True, blank=True

    )
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
    canton = GroupedForeignKey(
        Canton, 'provincia', null=True, blank=True
    )
    direccion = models.CharField(max_length=255, blank=True)
    sector = models.CharField(max_length=200, null=True, blank=True)
    horario_de_atencion_inicio_1 = models.TimeField(verbose_name="Hora de atención 1", blank=True)
    horario_de_atencion_fin_1 = models.TimeField(verbose_name="Hora de cierre 1", blank=True)
    horario_de_atencion_inicio_2 = models.TimeField(verbose_name="Hora de atención 2", blank=True)
    horario_de_atencion_fin_2 = models.TimeField(verbose_name="Hora de cierre 1", blank=True)

    horario_de_atencion_inicio_3 = models.TimeField(verbose_name="Hora de atención 3", blank=True)
    horario_de_atencion_fin_3 = models.TimeField(verbose_name="Hora de cierre 3", blank=True)
    telefono = models.CharField(max_length=10, verbose_name="Teléfono", blank=True)
    celular = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    latitud = models.DecimalField(max_digits=15, decimal_places=9, blank=True, )
    longitud = models.DecimalField(max_digits=15, decimal_places=9, blank=True, )
    prioridad = models.SmallIntegerField(default=1, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("locales", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Local, self).save(*args, **kwargs)


class ImagenLocal(models.Model):
    local = models.ForeignKey(Local, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='locales')

    class Meta:
        verbose_name = "Imágen de locales"
        verbose_name_plural = "Imágenes de locales"


class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"
