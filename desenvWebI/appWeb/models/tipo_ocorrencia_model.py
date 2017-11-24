# -*- coding: utf-8 -*-
from django.db import models

class TipoOcorrenciaModel(models.Model):
    nome = models.CharField(max_length=80)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'appWeb'
        verbose_name = 'Tipo Ocorrência'
        verbose_name_plural = 'Tipo Ocorrência'