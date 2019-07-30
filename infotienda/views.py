import random

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import DetailView

from infotienda.models import Canton, Categorias, Subcategorias, Local, ConfiguracioSitio, Provincia, Subscribe


# Create your views here.

def constant():
    valores = {}
    configuracion = ConfiguracioSitio.objects.get()
    categorias = Categorias.objects.all().order_by('nombre')
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
    valores["random"] = random.randint(100, 1000) * 5
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


def privacidad(request):
    constants = constant()
    return render(request, 'listing/privacidad.html', {'constants': constants})


def agregar(request):
    constants = constant()
    return render(request, 'listing/agregar.html', {'constants': constants})


class busqueda(View):
    def get(self, request):
        return redirect('/')

    def post(self, request):
        language = 'spanish'
        valor = request.POST['query']
        ciudad = request.POST['choices-single-defaul']
        # locales = Local.objects.annotate(
        #     search=SearchRank(vector, query),
        # ).filter(search=valor).filter(canton=ciudad).filter(publicado=True).order_by('prioridad')
        # ciudad = Canton.objects.get(id=ciudad)
        vector = SearchVector('nombre',  weight='A',config=language) + SearchVector('servicio', weight='B',config=language)
        query = SearchQuery(valor,config=language)
        locales= Local.objects.annotate(
            rank=SearchRank(vector, query)
        ).filter(rank__gte=0.1).filter(canton=ciudad).filter(publicado=True).order_by('prioridad').query
        print(locales)
        locales = Local.objects.annotate(
            rank=SearchRank(vector, query)
        ).filter(rank__gte=0.1).filter(canton=ciudad).filter(publicado=True).order_by('prioridad')
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
    return redirect("/")


def ingresarlocal(request):
    print("ingreso al metodo")
    if request.method == 'POST':
        nombre = request.POST['nombre']
        servicio = request.POST['servicio']
        telefono = request.POST['telefono']
        email = request.POST['email']

        Local.objects.create(nombre=nombre, servicio=servicio, telefono=telefono,
                             email=email, direccion=' ', sector='', horario_de_atencion_fin_1='00:00',
                             horario_de_atencion_inicio_1='00:00', horario_de_atencion_fin_2='00:00',
                             horario_de_atencion_inicio_2='00:00', horario_de_atencion_fin_3='00:00',
                             horario_de_atencion_inicio_3='00:00', latitud=0.00, longitud=0.00, publicado=False)
        ctx = {
            'nombre': nombre,
            'servicio': servicio,
            'telefono': telefono,
            'email': email,
        }
        html_part = render_to_string('email/email.html', ctx)
        send_mail(subject='INGRESO LOCAL: ' +nombre ,message='', from_email='contacto@infotiendaecuador.com',
                  recipient_list= [email,'anymaz@gmail.com'], fail_silently=False,
                  html_message=html_part)

        # ctx = {
        #     'nombres': estudiante.usuario.get_full_name(),
        #
        #     'curso': _curso,
        #     'actividad': 'lección',
        # }
        # html_part = render_to_string('email/reservacion.html', ctx)
        # send_mail('RESERVACIÓN ' + estudiante.usuario.get_full_name(), ' ', 'contacto@infotiendaecuador.com',
        #           [estudiante.usuario.email], fail_silently=False,
        #           html_message=html_part)
        #
        #

        # SendSubscribeMail(email) # Send the Mail, Class available in utils.py

    return redirect("/")
