from django.forms import ModelForm

from .models import Local


class LocalForm(ModelForm):
    class Meta:
        model = Local
        fields = ['nombre', 'servicio', 'imagen', 'categoria', 'subcategoria', 'provincia', 'canton', 'direccion',
                  'sector',
                  'horario_de_atencion_inicio_1', 'horario_de_atencion_fin_1', 'horario_de_atencion_inicio_2',
                  'horario_de_atencion_fin_2',
                  'horario_de_atencion_inicio_3', 'horario_de_atencion_fin_3', 'telefono', 'celular', 'email',
                  'facebook', 'twitter', 'instagram', 'whatsapp']
        labels = {
            'nombre': 'Nombre del local',
            'horario_de_atencion_inicio_1': 'Horario de apertura entre semana',
            'horario_de_atencion_fin_1': 'Horario de cierre entre semana',
            'horario_de_atencion_inicio_2': 'Horario de apertura en sábado',
            'horario_de_atencion_fin_2': 'Horario de cierre en sábado',
            'horario_de_atencion_inicio_3': 'Horario de apertura en domingo',
            'horario_de_atencion_fin_3': 'horario de cierre en domingo',

        }
