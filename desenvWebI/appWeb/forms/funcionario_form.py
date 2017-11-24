# coding: utf-8
from django import forms
from django.contrib.auth.hashers import make_password
from appWeb.models import TipoFuncionarioModel
from appWeb.models.funcionario_model import FuncionarioModel


class FuncionarioForm(forms.ModelForm):
    funcao = forms.ModelChoiceField(queryset=TipoFuncionarioModel.objects.all().exclude(excluido=True))

    class Meta:
        model = FuncionarioModel
        fields = ('first_name',
                  'last_name',
                  'email',
                  'username',
                  'password',
                  'matricula',
                  'funcao',
                  'coordenador',)
        exclude = ['excluido']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        instance = super(FuncionarioForm, self).save(commit=False)
        instance.password = make_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance