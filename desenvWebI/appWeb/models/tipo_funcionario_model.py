# -*- coding: utf-8 -*-
from django.db import models

class TipoFuncionarioModel(models.Model):
    descricao = models.CharField(max_length=50)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Tipo Funcionario'
        verbose_name_plural = 'Tipo Funcionários'