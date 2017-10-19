from django.contrib import admin

from easy_select2 import select2_modelform

from .models import (
    PessoasEnvolvidasAgenda,
    DepartamentoSetor,
    Esfera,
    OrgaoDemandante,
    AgendaAdministrativa,
    AgendaAnexos,
    AgendaTipo,
    AgendaMovimentacao
    )


from atividades.forms import AgendaAdministrativaAdminForm

AgendaForm = select2_modelform(AgendaAdministrativa,
                               form_class=AgendaAdministrativaAdminForm,
                               attrs={'width': '350px'})


@admin.register(PessoasEnvolvidasAgenda)
class PessoasEnvolvidasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'funcionario')
    search_fields = ('nome', 'funcionario',)
    ordering = ['nome']


@admin.register(DepartamentoSetor)
class AdminDepartamentoSetor(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ['nome']


@admin.register(Esfera)
class AdminEsfera(admin.ModelAdmin):
    list_display = ('esfera',)
    search_fields = ('esfera',)


@admin.register(OrgaoDemandante)
class AdminOrgaoDemandante(admin.ModelAdmin):
    list_display = ('orgao', 'cidade', 'uf')
    ordering = ['orgao']


class LineAdminAgendaMovimentacao(admin.StackedInline):
    model = AgendaMovimentacao
    extra = 1

    def get_extra(self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra


class LineAdminAgendaAnexos(admin.StackedInline):
    model = AgendaAnexos
    extra = 1

    def get_extra(self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra


@admin.register(AgendaAdministrativa)
class AdminAgendaAdministrativa(admin.ModelAdmin):
    form = AgendaForm
    list_display = ('pauta', 'dt_referencia', 'tipo_agenda', 'coordenador_agenda', 'status', 'prioridade', 'dt_prev_fim_agenda')
    list_editable = ('status',)
    radio_fields = {"status": admin.HORIZONTAL}
    # filter_horizontal = ('pessoas_envolvidas',)
    inlines = [LineAdminAgendaAnexos, LineAdminAgendaMovimentacao]

@admin.register(AgendaAnexos)
class AdminAgendaAnexo(admin.ModelAdmin):
    list_display = ('agenda_administrativa', 'descricao', 'anexo')


@admin.register(AgendaTipo)
class AdminAgendaTipo(admin.ModelAdmin):
    list_display = ('tipo',)
    ordering = ['tipo']
