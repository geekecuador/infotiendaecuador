from django.contrib.postgres.search import SearchVector
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from infotienda.models import Canton, Categorias, Subcategorias, Local, ConfiguracioSitio, Provincia, Subscribe


# Create your views here.

def constant():
    valores = {}
    configuracion = ConfiguracioSitio.objects.get()
    categorias = Categorias.objects.all()
    categorias_count = categorias.count()
    subcategorias_count = Subcategorias.objects.count()
    locals = Local.objects.count()
    ciudades = Canton.objects.all()
    provincias = Provincia.objects.all()
    valores["subcategorias_count"] = subcategorias_count
    valores["categorias_count"] = categorias_count
    valores["categorias"] = categorias
    valores["locals"] = locals
    valores["configuracion"] = configuracion
    valores["ciudades"] = ciudades
    valores["provincias"] = provincias
    return valores


class Locales(DetailView):
    model = Local
    template_name = "listing/single.html"

    # pk_url_kwarg = "post_id"
    def get_context_data(self, **kwargs):
        context = super(Locales, self).get_context_data(**kwargs)
        context['constants'] = constant()
        return context



def locales(request, nombre):
    print("Nombre: ")
    print(nombre)
    return render(request, 'listing/single.html', {})


def index(request):
    cantones = Canton.objects.all()
    import random
    fondo = random.randrange(1, 15, 1)
    fondo = 'fondo' + str(fondo) + '.jpeg'
    return render(request, 'index.html', {'cantones': cantones, 'fondo': fondo})


# Create your views here.
def single(request):
    return render(request, 'listing/single.html', {})


class busqueda(View):
    def get(self, request):
        return redirect('/')

    def post(self, request):
        valor = request.POST['query']
        ciudad = request.POST['choices-single-defaul']
        locales = Local.objects.annotate(
            search=SearchVector('nombre', 'servicio'),
        ).filter(search=valor).filter(canton=ciudad).filter(publicado=True)
        ciudad = Canton.objects.get(id=ciudad)
        constants = constant()
        return render(request, 'listing/listing.html',
                      {'valor': valor, 'ciudad': ciudad, 'constants': constants, 'locales': locales})


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['emailmailchimp']
        print("Email:")
        print(email)
        email_qs = Subscribe.objects.filter(email=email)
        if email_qs.exists():
            data = {"status": "404"}
            return JsonResponse(data)
        else:
            Subscribe.objects.create(email=email)
            # SendSubscribeMail(email) # Send the Mail, Class available in utils.py
            return redirect("/admin")
    return redirect("/")
