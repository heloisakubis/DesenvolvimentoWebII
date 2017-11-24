# coding: utf-8
from django import forms
from appWeb.models.tipo_ocorrencia_model import TipoOcorrenciaModel


class TipoOcorrenciaForm(forms.ModelForm):

    class Meta:
        model = TipoOcorrenciaModel
        exclude = ['excluido']