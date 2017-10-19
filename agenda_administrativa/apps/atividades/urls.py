from django.conf.urls import url

from .views import (
    # pessoas
    PessoaEnvolvidaListView,
    PessoaEnvolvidaCreateView,
    PessoaEnvolvidaUpdateView,
    PessoaEnvolvidaDeleteView,

    # depto-setor
    DeptoSetorListView,
    DeptoSetorCreateView,
    DeptoSetorUpdateView,
    DeptoSetorDeleteView,

    # Esfera
    EsferaListView,
    EsferaCreateView,
    EsferaUpdateView,
    EsferaDeleteView,

    # orgao demandante
    OrgaoDemandanteListView,
    OrgaoDemandanteCreateView,
    OrgaoDemandateUpdateView,
    OrgaoDemandanteDeleteView,

    # agenda tipo
    AgendaTipoListView,
    AgendaTipoCreateView,
    AgendaTipoUpdateView,
    AgendaTipoDeleteView,

    # Agenda Administrativa
    AgendaCompartilhadaListView,
    #AgendaCompartilhadaDetailView,

    # Agenda movimentacao
    agenda_detail,
    AgendaEncerradaDetail,
    AgendaAdministrativaCreateView,
    #AgendaCompartilhadaDetailView,
    AgendaEncerraRedirectView
)

urlpatterns = [
    # post views
    # pessoas
    url(r'^pessoas/$', PessoaEnvolvidaListView.as_view(), name='pessoa_envolvida_list'),
    url(r'^pessoas/create/$', PessoaEnvolvidaCreateView.as_view(), name='pessoa_envolvida_create'),
    url(r'^pessoas/update/(?P<pk>\d+)$', PessoaEnvolvidaUpdateView.as_view(), name='pessoa_envolvida_update'),
    url(r'^pessoas/delete/(?P<pk>\d+)$', PessoaEnvolvidaDeleteView.as_view(), name='pessoa_envolvida_delete'),

    # depto setor
    url(r'^depto-setor/$', DeptoSetorListView.as_view(), name='depto_setor_list'),
    url(r'^depto-setor/create/$', DeptoSetorCreateView.as_view(), name='depto_setor_create'),
    url(r'^depto-setor/update/(?P<pk>\d+)$', DeptoSetorUpdateView.as_view(), name='depto_setor_update'),
    url(r'^depto-setor/delete/(?P<pk>\d+)$', DeptoSetorDeleteView.as_view(), name='depto_setor_delete'),

    # esfera
    url(r'^esfera/$', EsferaListView.as_view(), name='esfera_list'),
    url(r'^esfera/create/$', EsferaCreateView.as_view(), name='esfera_create'),
    url(r'^esfera/update/(?P<pk>\d+)$', EsferaUpdateView.as_view(), name='esfera_update'),
    url(r'^esfera/delete/(?P<pk>\d+)$', EsferaDeleteView.as_view(), name='esfera_delete'),

   # orgao demandante
    url(r'^orgao-demandante/$', OrgaoDemandanteListView.as_view(), name='orgao_demandante_list'),
    url(r'^orgao-demandante/create/$', OrgaoDemandanteCreateView.as_view(), name='orgao_demandante_create'),
    url(r'^orgao-demandante/update/(?P<pk>\d+)$', OrgaoDemandateUpdateView.as_view(), name='orgao_demandate_update'),
    url(r'^orgao-demandante/delete/(?P<pk>\d+)$', OrgaoDemandanteDeleteView.as_view(), name='orgao_demandante_delete'),

   # orgao demandante
    url(r'^agenda-tipo/$', AgendaTipoListView.as_view(), name='agenda_tipo_list'),
    url(r'^agenda-tipo/create/$', AgendaTipoCreateView.as_view(), name='agenda_tipo_create'),
    url(r'^agenda-tipo/update/(?P<pk>\d+)$', AgendaTipoUpdateView.as_view(), name='agenda_tipo_update'),
    url(r'^agenda-tipo/delete/(?P<pk>\d+)$', AgendaTipoDeleteView.as_view(), name='agenda_tipo_delete'),

    # agenda administrativa
    url(r'^$', AgendaCompartilhadaListView.as_view(), name='agenda_compartilhada'),
    url(r'^agenda-detalhe/(?P<pk>\d+)$', agenda_detail, name='agenda_compartilhada_detail'),
    url(r'^agenda-encerrada/detalhe/(?P<pk>\d+)$', AgendaEncerradaDetail.as_view(), name='agenda_encerrada_detail'),
    
    #url(r'^agenda-movimentacao/create/$', AgendaMovimentacaoView.as_view(), name='agenda_movimentacao_create'),
    url(r'^agenda-administrativa/create/$', AgendaAdministrativaCreateView.as_view(), name='agenda_create'),
    url(r'^(?P<pk>\d+)/$', AgendaEncerraRedirectView.as_view(), name='encerra_agenda'),


]
