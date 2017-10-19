from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from ..models import (
    PessoasEnvolvidasAgenda,
    DepartamentoSetor,
    Esfera,
    OrgaoDemandante,
    AgendaTipo,
    AgendaAdministrativa,
    AgendaMovimentacao,
    AgendaAnexos
    )


from .serializers import (
    PessoasEnvolvidasSerializer,
    DepartamentoSetorSerializer,
    EsferaSerializer,
    OrgaoDemandanteSerializer,
    AgendaTipoSerializer,
    AgendaAdministrativaSerializer,
    AgendaMovimentacaoSerializer,
    AgendaAnexoSerializer
    )


class PessoasEnvolvidasAgendaViewSet(viewsets.ModelViewSet):
    """Pessoas envolvidas na agenda"""

    queryset = PessoasEnvolvidasAgenda.objects.all()
    serializer_class = PessoasEnvolvidasSerializer
    permission_classes = (IsAuthenticated,)


class DepartamentoSetorViewSet(viewsets.ModelViewSet):
    """Departamentos e setores envolvidos"""

    queryset = DepartamentoSetor.objects.all()
    serializer_class = DepartamentoSetorSerializer
    permission_classes = (IsAuthenticated,)


class EsferaViewSet(viewsets.ModelViewSet):
    """Esfera como união, municipio, etc..."""
    queryset = Esfera.objects.all()
    serializer_class = EsferaSerializer
    permission_classes = (IsAuthenticated,)


class OrgaoDemandanteViewSet(viewsets.ModelViewSet):
    """O orgão demandante da agenda"""
    queryset = OrgaoDemandante.objects.all()
    serializer_class = OrgaoDemandanteSerializer
    permission_classes = (IsAuthenticated,)


class AgendaTipoViewSet(viewsets.ModelViewSet):
    """o tipo de agenda"""
    queryset = AgendaTipo.objects.all()
    serializer_class = AgendaTipoSerializer
    permission_classes = (IsAuthenticated,)


class AgendaAdministrativaViewSet(viewsets.ModelViewSet):
    """A agenda administrativa"""


    queryset = AgendaAdministrativa.objects.all()
    serializer_class = AgendaAdministrativaSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['pauta']
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class AgendaMovimentacaoViewSet(viewsets.ModelViewSet):
    """Movimentação da agenda pelos usuários"""
    queryset = AgendaMovimentacao.objects.all()
    serializer_class = AgendaMovimentacaoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class AgendaAnexoViewSet(viewsets.ModelViewSet):
    """Anexos da agenda enviados pelos usuários"""
    queryset = AgendaAnexos.objects.all()
    serializer_class = AgendaAnexoSerializer
    permission_classes = (IsAuthenticated,)
