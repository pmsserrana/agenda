import datetime

from rest_framework import serializers
from ..models import (
    PessoasEnvolvidasAgenda,
    DepartamentoSetor,
    Esfera,
    OrgaoDemandante,
    AgendaTipo,
    AgendaAdministrativa,
    AgendaMovimentacao,
    AgendaAnexos,
)


class PessoasEnvolvidasSerializer(serializers.ModelSerializer):

    class Meta:
        model = PessoasEnvolvidasAgenda
        fields = ('id', 'nome', 'telefone', 'email', 'funcionario')


class DepartamentoSetorSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepartamentoSetor
        fields = ('id', 'nome')


class EsferaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Esfera
        fields = ('id', 'esfera')


class OrgaoDemandanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgaoDemandante
        fields = ('id', 'orgao', 'cidade', 'uf')


class AgendaTipoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgendaTipo
        fields = ('tipo',)


class AgendaAdministrativaSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgendaAdministrativa

        fields = ('id', 'usuario', 'dt_referencia', 'pauta',
                  'tipo_agenda', 'pessoas_envolvidas', 'inicio_acao',
                  'esfera', 'orgao_demandante', 'coordenador_agenda',
                  'status', 'prioridade', 'dpto_setor', 'fim_acao',
                  'dt_prev_dis_agenda', 'dt_prev_fim_agenda',
                  'dt_fim_agenda')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializers.save(usuario=self.request.user)


class AgendaMovimentacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgendaMovimentacao
        fields = ('usuario', 'desc_movimentacao', 'dt_atualizacao')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializers.save(usuario=self.request.user)


class AgendaAnexoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgendaAnexos
        fields = ('usuario', 'agenda_administrativa', 'descricao', 'anexo', 'dt_atualizacao')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializers.save(usuario=self.request.user)
