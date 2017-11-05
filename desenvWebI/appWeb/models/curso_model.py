# -*- coding: utf-8 -*-
from django.db import models

from appWeb.models.tipo_oferta_model import TipoOfertaModel


class CursoModel(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=200)
    duracao = models.CharField(max_length=2)
    oferta = models.ForeignKey(TipoOfertaModel, null=True, blank=True, related_name='_oferta_',
                              verbose_name='Oferta')

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'