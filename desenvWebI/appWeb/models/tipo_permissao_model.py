# -*- coding: utf-8 -*-
from django.db import models

class TipoPermissaoModel(models.Model):
    descricao = models.CharField(max_length=80)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        app_label = 'appWeb'
        verbose_name = 'Tipo Permissao'
        verbose_name_plural = 'Tipo Permissoes'