# coding: utf-8
from django import forms
from appWeb.models.tipo_oferta_model import TipoOfertaModel


class TipoOfertaForm(forms.ModelForm):

    class Meta:
        model = TipoOfertaModel
        exclude = ['excluido']