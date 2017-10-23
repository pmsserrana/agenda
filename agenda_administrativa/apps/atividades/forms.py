from django import forms
from django.forms import Textarea
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab, PrependedText, PrependedAppendedText
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, Layout, Div, Fieldset


from ckeditor.widgets import CKEditorWidget
from django_select2.forms import Select2Widget, Select2MultipleWidget
from .mixins import FormActionMixin

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


class PessoasEnvolvidasAgendaForm(FormActionMixin, forms.ModelForm):
    telefone = forms.CharField(label='telefone',widget=forms.TextInput(attrs={'placeholder': '(00) 000000000'}))
    def __init__(self, *args, **kwargs):
        super(PessoasEnvolvidasAgendaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'gravar'))
        self.helper.add_input(Submit('cancel', 'Cancelar',
                                     css_class='btn-danger',
                                     formnovalidate='formnovalidate',))
        self.helper.layout = Layout(
            Field('nome'),
            Field(PrependedText('telefone', '<i class="glyphicon glyphicon-earphone"></i>'), help_text='teste'),
            Field(PrependedText('email', '@')),
            Field('funcionario')           
        )
   
    class Meta:
        model = PessoasEnvolvidasAgenda
        fields = ('nome', 'telefone', 'email', 'funcionario')


class DepartamentoSetorForm(FormActionMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DepartamentoSetorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'gravar'))
        self.helper.add_input(Submit('cancel', 'Cancelar',
                                     css_class='btn-danger',
                                     formnovalidate='formnovalidate',))

    class Meta:
        model = DepartamentoSetor
        fields = ('nome',)


class EsferaForm(FormActionMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EsferaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'gravar'))
        self.helper.add_input(Submit('cancel', 'Cancelar',
                                     css_class='btn-danger',
                                     formnovalidate='formnovalidate',))

    class Meta:
        model = Esfera
        fields = ('esfera',)


class OrgaoDemandanteForm(FormActionMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrgaoDemandanteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'gravar'))
        self.helper.add_input(Submit('cancel', 'Cancelar',
                                     css_class='btn-danger',
                                     formnovalidate='formnovalidate',))

    class Meta:
        model = OrgaoDemandante
        fields = ('orgao', 'cidade', 'uf')


class AgendaTipoForm(FormActionMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AgendaTipoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'gravar'))
        self.helper.add_input(Submit('cancel', 'Cancelar',
                                     css_class='btn-danger',
                                     formnovalidate='formnovalidate',))

    class Meta:
        model = AgendaTipo
        fields = ('tipo',)


class AgendaAdministrativaForm(FormActionMixin, forms.ModelForm):
    dt_referencia = forms.DateField(label='data de referência', input_formats=["%d/%m/%Y", ], widget=forms.DateInput(format='%d/%m/%Y'))
    inicio_acao = forms.DateField(label='ínicio da ação', input_formats=["%d/%m/%Y", ], widget=forms.DateInput(format='%d/%m/%Y'))
    dt_prev_dis_agenda = forms.DateField(label='dt. prev. duscussão da agenda', input_formats=["%d/%m/%Y", ], widget=forms.DateInput(format='%d/%m/%Y'), required=False)
    dt_prev_fim_agenda = forms.DateField(label='dt. prev. fim da agenda', input_formats=["%d/%m/%Y", ], widget=forms.DateInput(format='%d/%m/%Y'))
    pauta = forms.CharField(widget=CKEditorWidget())
    # tipo_agenda = forms.CharField(widget=Select2Widget)
    compartilhada = forms.TypedChoiceField(label='compartilhada', coerce=lambda x: x =='True', choices=((True, 'Sim'), (False, 'Não')), widget=forms.RadioSelect, initial=True)

    def __init__(self, *args, **kwargs):
        super(AgendaAdministrativaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'gravar'))
        self.helper.add_input(Submit('cancel', 'Cancelar',
                                     css_class='btn-danger',
                                     formnovalidate='formnovalidate',))

        self.helper.layout = Layout(
          TabHolder(
              Tab('Pauta',
                InlineRadios('compartilhada'),
                Field(PrependedText('dt_referencia', '<i class="glyphicon glyphicon-calendar"></i>'), css_class='datepicker'),
                'pauta'),

              Tab('Outras Informações',
                'tipo_agenda',
                'pessoas_envolvidas',
                PrependedText('inicio_acao', '<i class="glyphicon glyphicon-calendar"></i>'),
                'esfera',
                'orgao_demandante',
                'coordenador_agenda',
                InlineRadios('prioridade'),
                'dpto_setor',
                PrependedText('fim_acao', '<i class="glyphicon glyphicon-calendar"></i>'),
                PrependedText('dt_prev_dis_agenda', '<i class="glyphicon glyphicon-calendar"></i>'),
                PrependedText('dt_prev_fim_agenda', '<i class="glyphicon glyphicon-calendar"></i>'))

          )) 

    class Meta:
        model = AgendaAdministrativa

        fields = (
                  'compartilhada',
                  'dt_referencia',
                  'pauta',
                  'tipo_agenda',
                  'pessoas_envolvidas',
                  'inicio_acao',
                  'esfera',
                  'orgao_demandante',
                  'coordenador_agenda',
                  'prioridade',
                  'dpto_setor',
                  'dt_prev_dis_agenda',
                  'dt_prev_fim_agenda',
                  )
        widgets = {
            'tipo_agenda': Select2Widget,
            'esfera': Select2Widget,
            'pessoas_envolvidas': Select2MultipleWidget,
            'orgao_demandante': Select2Widget,
            'coordenador_agenda': Select2Widget,
            'dpto_setor': Select2Widget,
        }


class AgendaAdministrativaAdminForm(forms.ModelForm):

    # status = forms.BooleanField(widget=forms.RadioSelect())

    class Meta:
        model = AgendaAdministrativa
        fields = ('compartilhada',
                  'dt_referencia',
                  'pauta',
                  'tipo_agenda',
                  'pessoas_envolvidas',
                  'inicio_acao',
                  'esfera',
                  'orgao_demandante',
                  'coordenador_agenda',
                  'status',
                  'prioridade',
                  'dpto_setor',
                  'fim_acao',
                  'dt_prev_dis_agenda',
                  'dt_prev_fim_agenda',
                  'dt_fim_agenda'
                  )


class AgendaMovimentacaoForm(forms.ModelForm):
    desc_movimentacao = forms.CharField(widget=CKEditorWidget(attrs={'cols': 80, 'rows': 4}))

    class Meta:
        model = AgendaMovimentacao
        fields = ('desc_movimentacao',)


class AgendaAnexoForm(forms.ModelForm):
    anexo = forms.FileField()

    class Meta:
        model = AgendaAnexos
        fields = ('descricao', 'anexo')
