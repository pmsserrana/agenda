# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 11:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaAdministrativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compartilhada', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Compartilhar agenda?')),
                ('dt_referencia', models.DateField(verbose_name='data de referência')),
                ('pauta', models.TextField(verbose_name='pauta')),
                ('inicio_acao', models.DateField(verbose_name='ínicio da ação')),
                ('status', models.BooleanField(choices=[(True, 'aberta'), (False, 'encerrada')], default=True, verbose_name='status')),
                ('prioridade', models.IntegerField(choices=[(0, 'baixa'), (1, 'média'), (2, 'alta')], default=1, verbose_name='prioridade')),
                ('fim_acao', models.DateField(blank=True, null=True, verbose_name='fim da ação')),
                ('dt_prev_dis_agenda', models.DateField(blank=True, null=True, verbose_name='data prev. discussão da agenda')),
                ('dt_prev_fim_agenda', models.DateField(blank=True, null=True, verbose_name='data prev. fim agenda')),
                ('dt_fim_agenda', models.DateField(blank=True, null=True, verbose_name='data finalização agenda')),
            ],
            options={
                'verbose_name': 'Agenda Administrativa',
                'verbose_name_plural': 'Agendas Administrativas',
                'db_table': 'tb_agenda_administrativa',
            },
        ),
        migrations.CreateModel(
            name='AgendaAnexos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=80, verbose_name='descrição')),
                ('anexo', models.FileField(blank=True, help_text='anexos para agendas', max_length=200, null=True, upload_to='uploads/anexos/', verbose_name='enviar arquivo')),
                ('dt_atualizacao', models.DateTimeField(auto_now_add=True, verbose_name='data atualizacao')),
                ('agenda_administrativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anexos', to='atividades.AgendaAdministrativa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anexos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Agenda Anexo',
                'verbose_name_plural': 'Agenda Anexos',
                'db_table': 'tb_agenda_anexo',
            },
        ),
        migrations.CreateModel(
            name='AgendaMovimentacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_movimentacao', models.TextField(blank=True, null=True, verbose_name='Movimentação')),
                ('dt_atualizacao', models.DateTimeField(auto_now_add=True, verbose_name='data atualizacao')),
                ('agenda_administrativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividades.AgendaAdministrativa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimentacao', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Agenda Movimentacao',
                'verbose_name_plural': 'Agendas Movimentacao',
                'db_table': 'tb_agenda_movimentacao',
            },
        ),
        migrations.CreateModel(
            name='AgendaTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=60, verbose_name='tipo')),
            ],
            options={
                'verbose_name': 'Agenda Tipo',
                'verbose_name_plural': 'Agendas Tipo',
                'db_table': 'tb_agenda_agenda_tipo',
            },
        ),
        migrations.CreateModel(
            name='DepartamentoSetor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'Departamento ou Setor',
                'verbose_name_plural': 'Departamentos ou Setores',
                'db_table': 'tb_agenda_departamento_setor',
            },
        ),
        migrations.CreateModel(
            name='Esfera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esfera', models.CharField(max_length=60, verbose_name='esfera')),
            ],
            options={
                'verbose_name': 'Esfera',
                'verbose_name_plural': 'Esfera',
                'db_table': 'tb_agenda_esfera',
            },
        ),
        migrations.CreateModel(
            name='OrgaoDemandante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgao', models.CharField(max_length=60, verbose_name='orgão')),
                ('cidade', models.CharField(max_length=80, verbose_name='cidade')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='uf')),
            ],
            options={
                'verbose_name': 'Orgão demandante',
                'verbose_name_plural': 'Orgãos demandantes',
                'db_table': 'tb_agenda_orgao',
            },
        ),
        migrations.CreateModel(
            name='PessoasEnvolvidasAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, unique=True, verbose_name='nome')),
                ('telefone', models.CharField(max_length=15, verbose_name='telefone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('funcionario', models.BooleanField(choices=[(True, 'sim'), (False, 'não')], verbose_name='é funcionario?')),
            ],
            options={
                'verbose_name': 'Pessoa envolvida',
                'verbose_name_plural': 'Pessoas envolvidas',
                'db_table': 'tb_pessoa_envolvida',
            },
        ),
        migrations.AddField(
            model_name='agendaadministrativa',
            name='coordenador_agenda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coordenador', to='atividades.PessoasEnvolvidasAgenda'),
        ),
        migrations.AddField(
            model_name='agendaadministrativa',
            name='dpto_setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividades.DepartamentoSetor'),
        ),
        migrations.AddField(
            model_name='agendaadministrativa',
            name='esfera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividades.Esfera'),
        ),
        migrations.AddField(
            model_name='agendaadministrativa',
            name='orgao_demandante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividades.OrgaoDemandante'),
        ),
        migrations.AddField(
            model_name='agendaadministrativa',
            name='pessoas_envolvidas',
            field=models.ManyToManyField(related_name='pessoas', to='atividades.PessoasEnvolvidasAgenda'),
        ),
        migrations.AddField(
            model_name='agendaadministrativa',
            name='tipo_agenda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividades.AgendaTipo'),
        ),
        migrations.AddField(
            model_name='agendaadministrativa',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendas', to=settings.AUTH_USER_MODEL),
        ),
    ]
