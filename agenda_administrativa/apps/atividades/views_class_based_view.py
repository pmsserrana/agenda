class AgendaCompartilhadaDetailView(LoginRequiredMixin, DetailView):
    model = AgendaAdministrativa
    context_object_name = 'agenda_compartilhada'
    template_name = 'agenda/agenda_administrativa/agenda_detail.html'

    def get_context_data(self, **kwargs):

        # context time
        context = super(AgendaCompartilhadaDetailView, self).get_context_data(**kwargs)
        date1 = AgendaAdministrativa.objects.values_list('dt_prev_fim_agenda', flat=True).get(pk = self.kwargs['pk'])
        date2 = AgendaAdministrativa.objects.values_list('inicio_acao', flat=True).get(pk = self.kwargs['pk'])

        difftime = date1 - date2
        difftime = difftime.days

        context['tempo_restante'] = difftime

        if (difftime < 15) and (difftime > 10):
            context['cor_periodo'] = 'bg-yellow'
            context['info_icon'] = 'glyphicon-warning-sign'

        elif (difftime > 5) and (difftime <= 10):
            context['cor_periodo'] = 'bg-red'
            context['info_icon'] = 'glyphicon-thumbs-down'

        else:
            context['cor_periodo'] = 'bg-green'
            context['info_icon'] = 'glyphicon-thumbs-up'

        # context movimentacao
        # agenda = AgendaAdministrativa.objects.only('id').get(pk=self.kwargs['pk'])
        # movimento = AgendaMovimentacao.objects.select_related().get(pk=agenda.id)
        return context
