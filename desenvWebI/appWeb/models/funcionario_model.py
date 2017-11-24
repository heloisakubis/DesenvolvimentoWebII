# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from appWeb.models.tipo_funcionario_model import TipoFuncionarioModel


class FuncionarioModel(User):
    matricula = models.CharField(max_length=20)
    funcao = models.ForeignKey(TipoFuncionarioModel, verbose_name='Função')
    excluido = models.BooleanField(default=False)
    coordenador = models.BooleanField(default=False)

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionários'