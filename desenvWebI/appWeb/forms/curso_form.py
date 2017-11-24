# coding: utf-8
from django import forms
from appWeb.models.curso_model import CursoModel
from appWeb.models.funcionario_model import FuncionarioModel
from appWeb.models.tipo_oferta_model import TipoOfertaModel


class CursoForm(forms.ModelForm):
    oferta = forms.ModelChoiceField(queryset=TipoOfertaModel.objects.all().exclude(excluido=True))
    coordenador= forms.ModelChoiceField(queryset=FuncionarioModel.objects.filter(funcao__nome__exact='Professor').exclude(excluido=True))

    class Meta:
        model = CursoModel
        exclude = ['excluido']
        widgets = {
            'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }