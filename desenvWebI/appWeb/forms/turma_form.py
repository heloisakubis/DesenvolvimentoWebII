# coding: utf-8
from django import forms
from appWeb.models.turma_model import TurmaModel


class TurmaForm(forms.ModelForm):

    class Meta:
        model = TurmaModel
        exclude = ['excluido']
        widgets = {
            'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }