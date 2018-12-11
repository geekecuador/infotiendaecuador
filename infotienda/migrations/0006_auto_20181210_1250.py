# Generated by Django 2.1.3 on 2018-12-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infotienda', '0005_auto_20181210_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redsocial',
            name='local',
        ),
        migrations.AddField(
            model_name='local',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='local',
            name='instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='local',
            name='twitter',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='local',
            name='whatsapp',
            field=models.URLField(blank=True),
        ),
        migrations.DeleteModel(
            name='RedSocial',
        ),
    ]
