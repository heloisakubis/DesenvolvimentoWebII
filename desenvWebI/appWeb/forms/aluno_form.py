# coding: utf-8
from django import forms
from appWeb.models.aluno_model import AlunoModel
from appWeb.models.turma_model import TurmaModel
from appWeb.models.curso_model import CursoModel



class AlunoForm(forms.ModelForm):
    turma = forms.ModelChoiceField(queryset=TurmaModel.objects.all().exclude(excluido=True))
    curso = forms.ModelChoiceField(queryset=CursoModel.objects.all().exclude(excluido=True))

    class Meta:
        model = AlunoModel
        exclude = ['excluido']
