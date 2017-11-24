# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import now

from appWeb.models.aluno_model import AlunoModel
from appWeb.models.funcionario_model import FuncionarioModel
from appWeb.models.tipo_ocorrencia_model import TipoOcorrenciaModel


class OcorrenciaModel(models.Model):
    aluno = models.ForeignKey(AlunoModel)
    tipo_ocorrencia = models.ForeignKey(TipoOcorrenciaModel)
    data_ocorrencia = models.DateField(default=now)
    hora_ocorrencia = models.TimeField(default=now)
    motivo = models.TextField(max_length=150)
    funcionario = models.ForeignKey(FuncionarioModel, null=True)
    excluido = models.BooleanField(default=False)


    def __unicode__(self):
        return self.aluno

    def __str__(self):
        return self.aluno

    class Meta:
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'