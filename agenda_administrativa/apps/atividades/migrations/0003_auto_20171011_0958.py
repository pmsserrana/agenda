# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0002_auto_20171011_0934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendaanexos',
            options={'ordering': ('-dt_atualizacao',), 'verbose_name': 'Agenda Anexo', 'verbose_name_plural': 'Agenda Anexos'},
        ),
    ]
