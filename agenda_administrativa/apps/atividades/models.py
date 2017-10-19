import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class PessoasEnvolvidasAgenda(models.Model):
    FUNCIONARIO_CHOICES = (
        (True, 'sim'),
        (False, 'não'),
    )

    nome = models.CharField('nome', max_length=80, unique=True)
    telefone = models.CharField('telefone', max_length=15)
    email = models.EmailField('email', blank=True, null=True)
    funcionario = models.BooleanField('é funcionario?', choices=FUNCIONARIO_CHOICES)

    class Meta:
        verbose_name = 'Pessoa envolvida'
        verbose_name_plural = 'Pessoas envolvidas'
        db_table = 'tb_pessoa_envolvida'

    def __str__(self):
        return self.nome


class DepartamentoSetor(models.Model):

    nome = models.CharField('nome', max_length=80)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Departamento ou Setor'
        verbose_name_plural = 'Departamentos ou Setores'
        db_table = 'tb_agenda_departamento_setor'


class Esfera(models.Model):
    esfera = models.CharField('esfera', max_length=60)

    def __str__(self):
        return self.esfera

    class Meta:
        verbose_name = 'Esfera'
        verbose_name_plural = 'Esfera'
        db_table = 'tb_agenda_esfera'


class OrgaoDemandante(models.Model):
    STATE_CHOICES = (('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
                     ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
                     ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
                     ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
                     ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
                     ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
                     ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
                     ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
                     ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
                     ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'))

    orgao = models.CharField('orgão', max_length=60)
    cidade = models.CharField('cidade', max_length=80)
    uf = models.CharField('uf', max_length=2, choices=STATE_CHOICES)

    def __str__(self):
        return self.orgao

    class Meta:
        verbose_name = 'Orgão demandante'
        verbose_name_plural = 'Orgãos demandantes'
        db_table = 'tb_agenda_orgao'


class AgendaTipo(models.Model):
    tipo = models.CharField('tipo', max_length=60)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Agenda Tipo'
        verbose_name_plural = 'Agendas Tipo'
        db_table = 'tb_agenda_agenda_tipo'


class StatusManager(models.Manager):
    def get_queryset(self):
        return super(StatusManager, self).get_queryset().filter(status=True)


class PeriodoDuracaoAgendaManager(models.Manager):
    def get_periodo(self, result, dt_inicio, dt_final):
        result = self.dt_final - self.inicio_acao
        return result


class AgendaAdministrativa(models.Model):
    STATUS_CHOICES = (
        (True, 'aberta'),
        (False, 'encerrada'),
    )
    PRIORIDADE_CHOICES = (
        (0, 'baixa'),
        (1, 'média'),
        (2, 'alta'),
    )

    COMPARTILHAR_AGENDA = (
        (True, 'Sim'),
        (False, 'Não')
    )

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agendas')
    compartilhada = models.BooleanField('Compartilhar agenda?', choices=COMPARTILHAR_AGENDA)
    dt_referencia = models.DateField('data de referência')
    pauta = models.TextField('pauta')
    tipo_agenda = models.ForeignKey(AgendaTipo, on_delete=models.CASCADE)
    pessoas_envolvidas = models.ManyToManyField(PessoasEnvolvidasAgenda, related_name='pessoas')
    inicio_acao = models.DateField('ínicio da ação')
    esfera = models.ForeignKey(Esfera, on_delete=models.CASCADE)
    orgao_demandante = models.ForeignKey(OrgaoDemandante, on_delete=models.CASCADE)
    coordenador_agenda = models.ForeignKey(PessoasEnvolvidasAgenda, related_name='coordenador', on_delete=models.CASCADE)
    status = models.BooleanField('status', choices=STATUS_CHOICES, default=True)
    prioridade = models.IntegerField('prioridade', choices=PRIORIDADE_CHOICES, default=1)
    dpto_setor = models.ForeignKey(DepartamentoSetor, on_delete=models.CASCADE)
    fim_acao = models.DateField('fim da ação', blank=True, null=True)
    dt_prev_dis_agenda = models.DateField('data prev. discussão da agenda', blank=True, null=True)
    dt_prev_fim_agenda = models.DateField('data prev. fim agenda', blank=True, null=True)
    dt_fim_agenda = models.DateField('data finalização agenda', blank=True, null=True)
    objects = models.Manager()  # manager padrão
    abertos = StatusManager()  # manager customizado para trazer as agendas abertas
    periodo = PeriodoDuracaoAgendaManager() # manager periodo duracao agenda

    def __str__(self):
        return self.pauta

    class Meta:
        verbose_name = 'Agenda Administrativa'
        verbose_name_plural = 'Agendas Administrativas'
        db_table = 'tb_agenda_administrativa'

    def close(self):
        self.status = False
        self.dt_fim_agenda = datetime.date.today()
        self.save()
        return reverse_lazy('atividades:agenda_compartilhada')

    def save(self, *args, **kwargs):
        if self.inicio_acao < self.dt_referencia:
            raise Exception('Inicio da ação não pode ser anterior a data de referência')
        super(AgendaAdministrativa, self).save(*args, **kwargs)

    
class AgendaMovimentacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='movimentacao')
    agenda_administrativa = models.ForeignKey(AgendaAdministrativa)
    desc_movimentacao = models.TextField('Movimentação', blank=True, null=True)
    dt_atualizacao = models.DateTimeField('data atualizacao', auto_now_add=True)

    def __str__(self):
        return self.desc_movimentacao

    class Meta:
        verbose_name = 'Agenda Movimentacao'
        verbose_name_plural = 'Agendas Movimentacao'
        db_table = 'tb_agenda_movimentacao'
        ordering = ('-dt_atualizacao',)

    
class AgendaAnexos(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='anexos')
    agenda_administrativa = models.ForeignKey(AgendaAdministrativa, related_name='anexos')
    descricao = models.CharField('descrição', max_length=80)
    anexo = models.FileField('enviar arquivo', max_length=200, upload_to='uploads/anexos/', blank=True, null=True,
                             help_text="anexos para agendas")
    dt_atualizacao = models.DateTimeField('data atualizacao', auto_now_add=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Agenda Anexo'
        verbose_name_plural = 'Agenda Anexos'
        db_table = 'tb_agenda_anexo'
        ordering = ('-dt_atualizacao',)

    def save_model(self, request, obj, form, change):
        if not obj.usuario.id:
            obj.usuario = request.user
        obj.save()
