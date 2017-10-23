from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from atividades.models import AgendaAdministrativa, AgendaMovimentacao

# print relatorio
@login_required(login_url='/login/')
def agenda_relatorio(request, pk):
    # agenda detail
    agenda_report = get_object_or_404(AgendaAdministrativa.objects, pk=pk)

    # filter movimentacao
    movimento = AgendaMovimentacao.objects.filter(agenda_administrativa=pk)

    template_name = 'agenda/agenda_administrativa/agenda_detail.html'
  
    return render(request,
                  template_name,
                  {'agenda_report': agenda_report,
                   'movimento': movimento})

