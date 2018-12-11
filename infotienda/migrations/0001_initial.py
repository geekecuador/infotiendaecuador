# Generated by Django 2.1.3 on 2018-12-10 03:40

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Cantón',
                'verbose_name_plural': 'Cantones',
            },
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='ImagenLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('servicio', models.TextField()),
                ('direccion', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=200)),
                ('horario_de_atencion_inicio_1', models.TimeField()),
                ('horario_de_atencion_fin_1', models.TimeField()),
                ('horario_de_atencion_inicio_2', models.TimeField()),
                ('horario_de_atencion_fin_2', models.TimeField()),
                ('telefono', models.CharField(max_length=10)),
                ('celular', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('longitud', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('latitud', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('prioridad', models.SmallIntegerField(blank=True, default=1)),
                ('publicado', models.BooleanField(default=False)),
                ('canton', smart_selects.db_fields.GroupedForeignKey(group_field='provincia', on_delete=django.db.models.deletion.CASCADE, to='infotienda.Canton')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='infotienda.Categorias')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialnetworks', to='infotienda.Local')),
            ],
            options={
                'verbose_name': 'Red social',
                'verbose_name_plural': 'Redes sociales',
            },
        ),
        migrations.CreateModel(
            name='Subcategorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infotienda.Categorias')),
            ],
            options={
                'verbose_name': 'Subcategoria',
                'verbose_name_plural': 'Subcategorias',
            },
        ),
        migrations.AddField(
            model_name='local',
            name='provincia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='infotienda.Provincia'),
        ),
        migrations.AddField(
            model_name='local',
            name='subcategoria',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='categorias', on_delete=django.db.models.deletion.CASCADE, to='infotienda.Subcategorias'),
        ),
        migrations.AddField(
            model_name='imagenlocal',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='infotienda.Local'),
        ),
        migrations.AddField(
            model_name='canton',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infotienda.Provincia'),
        ),
    ]
