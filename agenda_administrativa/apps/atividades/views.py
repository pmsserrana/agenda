import datetime
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
    FormView,
    RedirectView
)

from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect


from braces.views import LoginRequiredMixin

from .forms import (
    PessoasEnvolvidasAgendaForm,
    DepartamentoSetorForm,
    EsferaForm,
    OrgaoDemandanteForm,
    AgendaTipoForm,
    AgendaMovimentacaoForm,
    AgendaAnexoForm,
    AgendaAdministrativaForm
)

from .models import (
    PessoasEnvolvidasAgenda,
    DepartamentoSetor,
    Esfera,
    OrgaoDemandante,
    AgendaTipo,
    AgendaAdministrativa,
    AgendaMovimentacao,
    AgendaAnexos
)


# pessoas envolvidas CRUD
class PessoaEnvolvidaListView(LoginRequiredMixin, ListView):
    model = PessoasEnvolvidasAgenda
    template_name = 'agenda/pessoas/pessoas_envolvidas_list.html'
    context_object_name = 'pessoas'
    queryset = PessoasEnvolvidasAgenda.objects.all()


class PessoaEnvolvidaCreateView(LoginRequiredMixin, CreateView):
    model = PessoasEnvolvidasAgenda
    form_class = PessoasEnvolvidasAgendaForm
    template_name = 'agenda/pessoas/pessoa_create_form.html'

    success_url = reverse_lazy('atividades:pessoa_envolvida_list')


class PessoaEnvolvidaUpdateView(LoginRequiredMixin, UpdateView):
    model = PessoasEnvolvidasAgenda
    template_name = 'agenda/pessoas/pessoa_create_form.html'
    form_class = PessoasEnvolvidasAgendaForm

    success_url = reverse_lazy('atividades:pessoa_envolvida_list')


class PessoaEnvolvidaDeleteView(LoginRequiredMixin, DeleteView):
    model = PessoasEnvolvidasAgenda
    template_name = 'delete_base.html'
    success_url = reverse_lazy('atividades:pessoa_envolvida_list')


# Departamento Setor CRUD
class DeptoSetorListView(LoginRequiredMixin, ListView):
    model = DepartamentoSetor
    template_name = 'agenda/depto_setor/depto_setor_list.html'
    context_object_name = 'setores'
    queryset = DepartamentoSetor.objects.all()


class DeptoSetorCreateView(LoginRequiredMixin, CreateView):
    model = DepartamentoSetor
    form_class = DepartamentoSetorForm
    template_name = 'agenda/depto_setor/depto_setor_create_form.html'

    success_url = reverse_lazy('atividades:depto_setor_list')


class DeptoSetorUpdateView(LoginRequiredMixin, UpdateView):
    model = DepartamentoSetor
    template_name = 'agenda/depto_setor/depto_setor_create_form.html'
    form_class = DepartamentoSetorForm

    success_url = reverse_lazy('atividades:depto_setor_list')


class DeptoSetorDeleteView(LoginRequiredMixin, DeleteView):
    model = DepartamentoSetor
    template_name = 'delete_base.html'
    success_url = reverse_lazy('atividades:depto_setor_list')


# Esfera CRUD
class EsferaListView(LoginRequiredMixin, ListView):
    model = Esfera
    template_name = 'agenda/esfera/esfera_list.html'
    context_object_name = 'esferas'
    queryset = Esfera.objects.all()


class EsferaCreateView(LoginRequiredMixin, CreateView):
    model = Esfera
    form_class = EsferaForm
    template_name = 'agenda/esfera/esfera_create_form.html'

    success_url = reverse_lazy('atividades:esfera_list')


class EsferaUpdateView(LoginRequiredMixin, UpdateView):
    model = Esfera
    template_name = 'agenda/esfera/esfera_create_form.html'
    form_class = EsferaForm

    success_url = reverse_lazy('atividades:esfera_list')


class EsferaDeleteView(LoginRequiredMixin, DeleteView):
    model = Esfera
    template_name = 'delete_base.html'
    success_url = reverse_lazy('atividades:esfera_list')


# Orgao Demandante
class OrgaoDemandanteListView(LoginRequiredMixin, ListView):
    model = OrgaoDemandante
    template_name = 'agenda/orgao_demandante/orgao_demandante_list.html'
    context_object_name = 'orgao_demandante'
    queryset = OrgaoDemandante.objects.all()


class OrgaoDemandanteCreateView(LoginRequiredMixin, CreateView):
    model = OrgaoDemandante
    form_class = OrgaoDemandanteForm
    template_name = 'agenda/orgao_demandante/orgao_demandante_create_form.html'

    success_url = reverse_lazy('atividades:orgao_demandante_list')


class OrgaoDemandateUpdateView(LoginRequiredMixin, UpdateView):
    model = OrgaoDemandante
    template_name = 'agenda/orgao_demandante/orgao_demandante_create_form.html'
    form_class = OrgaoDemandanteForm

    success_url = reverse_lazy('atividades:orgao_demandante_list')


class OrgaoDemandanteDeleteView(LoginRequiredMixin, DeleteView):
    model = OrgaoDemandante
    template_name = 'delete_base.html'
    success_url = reverse_lazy('atividades:orgao_demandante_list')


# Agenda Tipo CRUD
class AgendaTipoListView(LoginRequiredMixin, ListView):
    model = AgendaTipo
    template_name = 'agenda/agenda_tipo/agenda_tipo_list.html'
    context_object_name = 'agenda_tipos'
    queryset = AgendaTipo.objects.all()


class AgendaTipoCreateView(LoginRequiredMixin, CreateView):
    model = AgendaTipo
    form_class = AgendaTipoForm
    template_name = 'agenda/agenda_tipo/agenda_tipo_create_form.html'

    success_url = reverse_lazy('atividades:agenda_tipo_list')


class AgendaTipoUpdateView(LoginRequiredMixin, UpdateView):
    model = AgendaTipo
    template_name = 'agenda/agenda_tipo/agenda_tipo_create_form.html'
    form_class = AgendaTipoForm

    success_url = reverse_lazy('atividades:agenda_tipo_list')


class AgendaTipoDeleteView(LoginRequiredMixin, DeleteView):
    model = AgendaTipo
    template_name = 'delete_base.html'
    success_url = reverse_lazy('atividades:agenda_tipo_list')


# Agenda Administrativa CRUD
class AgendaCompartilhadaListView(LoginRequiredMixin, ListView):
    model = AgendaAdministrativa
    template_name = 'agenda/agenda_administrativa/agenda_list.html'
    context_object_name = 'agendas'

    def get_context_data(self, **kwargs):
        aberta = True
        fechada = False
        baixa = 0
        media = 1
        alta = 2
        sim = True

        context = super(AgendaCompartilhadaListView, self).get_context_data(**kwargs)

        baixa = AgendaAdministrativa.objects.select_related().filter(prioridade=baixa, status=aberta, compartilhada=sim)
        context['baixa_prioridade'] = baixa
        context['count_baixa'] = baixa.count()

        media = AgendaAdministrativa.objects.select_related().filter(prioridade=media, status=aberta, compartilhada=sim)
        context['media_prioridade'] = media
        context['count_media'] = media.count()

        alta = AgendaAdministrativa.objects.select_related().filter(prioridade=alta, status=aberta, compartilhada=sim)
        context['alta_prioridade'] = alta
        context['count_alta'] = alta.count()

        encerrada = AgendaAdministrativa.objects.select_related().filter(status=fechada, compartilhada=sim)
        context['agendas_encerradas'] = encerrada
        context['count_encerrada'] = encerrada.count()

        return context


# detalhamento da Agenda
@login_required(login_url='/login/')
def agenda_detail(request, pk):
    # agenda detail
    agenda_detail = get_object_or_404(AgendaAdministrativa.objects.filter(status='True'), pk=pk)

    # filter movimentacao
    movimentacao = AgendaMovimentacao.objects.filter(agenda_administrativa=pk)

    anexos = AgendaAnexos.objects.filter(agenda_administrativa=pk)

     
    template_name = 'agenda/agenda_administrativa/agenda_detail.html'

    # time operations diff
    date1 = AgendaAdministrativa.objects.values_list('dt_prev_fim_agenda', flat=True).get(pk=pk)
    date2 = AgendaAdministrativa.objects.values_list('inicio_acao', flat=True).get(pk=pk)

    difftime = date1 - date2
    tempo_restante = difftime.days

    if (tempo_restante < 15) and (tempo_restante > 10):
        cor_periodo = 'bg-yellow'
        info_icon = 'glyphicon-warning-sign'

    elif (tempo_restante > 1) and (tempo_restante <= 10):
        cor_periodo = 'bg-red'
        info_icon = 'glyphicon-thumbs-down'

    elif tempo_restante > 15:
        cor_periodo = 'bg-green'
        info_icon = 'glyphicon-thumbs-up'
    else:
        cor_periodo = 'bg-red'
        info_icon = 'glyphicon-thumbs-down'

    # deal with forms
    atividade_form = AgendaMovimentacaoForm
    anexo_form = AgendaAnexoForm

    if request.method == 'POST':
        if 'gravar_movimentacao' in request.POST:
            atividade_form = AgendaMovimentacaoForm(request.POST, prefix="agenda_atividade")
            if atividade_form.is_valid():
                new_atividade = atividade_form.save(commit=False)
                new_atividade.agenda_administrativa = agenda_detail
                new_atividade.usuario = request.user
                new_atividade.save()
                return redirect('atividades:agenda_compartilhada_detail', pk)

            anexo_form = AgendaAnexoForm(prefix="agenda_anexo")

        elif 'gravar_anexo' in request.POST:
            anexo_form = AgendaAnexoForm(request.POST, request.FILES, prefix="agenda_anexo")

            if anexo_form.is_valid():
                new_anexo = anexo_form.save(commit=False)
                new_anexo.agenda_administrativa = agenda_detail
                new_anexo.usuario = request.user
                new_anexo.save()
                return redirect('atividades:agenda_compartilhada_detail', pk)
            
            atividade_form = AgendaMovimentacaoForm(prefix="agenda_atividade")
    else:
        atividade_form = AgendaMovimentacaoForm(prefix="agenda_atividade")
        anexo_form = AgendaAnexoForm(prefix="agenda_anexo")

    return render(request,
                  template_name,
                  {'agenda_detail': agenda_detail,
                   'tempo_restante': tempo_restante,
                   'cor_periodo': cor_periodo,
                   'info_icon': info_icon,
                   'atividade_form': atividade_form,
                   'anexo_form': anexo_form,
                   'movimentacao': movimentacao,
                   'anexos': anexos})


class AgendaEncerradaDetail(DetailView):
    model = AgendaAdministrativa
    template_name = 'agenda/agenda_administrativa/agenda_encerrada_detail.html'
    context_object_name = 'encerrada_detail'

    def get_context_data(self, **kwargs):
        context = super(AgendaEncerradaDetail, self).get_context_data(**kwargs)
        context['movimentacao'] = AgendaMovimentacao.objects.filter(agenda_administrativa=self.kwargs['pk'])
        context['anexos'] = AgendaAnexos.objects.filter(agenda_administrativa=self.kwargs['pk'])

        date1 = AgendaAdministrativa.objects.values_list('dt_fim_agenda', flat=True).get(pk=self.kwargs['pk'])
        date2 = AgendaAdministrativa.objects.values_list('inicio_acao', flat=True).get(pk=self.kwargs['pk'])  
        
        difftime = date1 - date2

        context['tempo_corrido'] = difftime.days

        return context

    def get_queryset(self):
        fechada = False
        sim = True
        encerradas = AgendaAdministrativa.objects.select_related().filter(status=fechada, compartilhada=sim)
        return encerradas


class AgendaAdministrativaCreateView(LoginRequiredMixin, CreateView):
    model = AgendaAdministrativa
    form_class = AgendaAdministrativaForm
    template_name = 'agenda/agenda_administrativa/agenda_create_form.html'

    success_url = reverse_lazy('atividades:agenda_compartilhada')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.status = True
        return super(AgendaAdministrativaCreateView, self).form_valid(form)


class AgendaAdministrativaUpdateView(LoginRequiredMixin, UpdateView):
    model = AgendaAdministrativa
    form_class = AgendaAdministrativaForm
    template_name = 'agenda/agenda_administrativa/agenda_create_form.html'

    success_url = reverse_lazy('atividades:agenda_compartilhada')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.status = True
        return super(AgendaAdministrativaCreateView, self).form_valid(form)


class AgendaDeleteView(LoginRequiredMixin, DeleteView):
    model = AgendaAdministrativa
    template_name = 'delete_base.html'
    success_url = reverse_lazy('atividades:agenda_compartilhada')


class AgendaEncerraRedirectView(RedirectView):

    def get_redirect_url(self, **kwargs):
        agenda_id = self.kwargs.get('pk')
        agenda = get_object_or_404(AgendaAdministrativa.objects.filter(status=True), pk=agenda_id)
        agenda.status = False
        agenda.dt_fim_agenda = datetime.date.today()
        agenda.save()
        return reverse('atividades:agenda_compartilhada')
