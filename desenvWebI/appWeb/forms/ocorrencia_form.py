# coding: utf-8
from django import forms
from appWeb.models.ocorrencia_model import OcorrenciaModel
from appWeb.models.aluno_model import AlunoModel


class OcorrenciaForm(forms.ModelForm):
    aluno = forms.ModelChoiceField(queryset=AlunoModel.objects.all().exclude(excluido=True))

    class Meta:
        model = OcorrenciaModel
        exclude = ['excluido', 'funcionario']
        widgets = {
            'motivo': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        }


TYPE_CHOICES = (
    ('nome', 'Nome'),
    ('matricula', 'Matricula'),
    ('turma', 'Turma'),
    ('curso', 'Curso'),
)


class AlunoSearchForm(forms.Form):
    name = forms.CharField()
    tipo = forms.Select(choices=TYPE_CHOICES)
