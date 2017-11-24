# coding: utf-8
from django import forms
from appWeb.models.tipo_funcionario_model import TipoFuncionarioModel


class TipoFuncionarioForm(forms.ModelForm):

    class Meta:
        model = TipoFuncionarioModel
        fields = '__all__'
        exclude = ['excluido']