# -*- coding: utf-8 -*-
from django.db import models
from appWeb.models.curso_model import CursoModel


class TurmaModel(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=100)
    ano = models.CharField(max_length=30)
    curso = models.ForeignKey(CursoModel, related_name='_curso_',
                              verbose_name='Curso')
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'appWeb'
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'