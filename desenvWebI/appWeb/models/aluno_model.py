# -*- coding: utf-8 -*-
from django.db import models

from appWeb.models.turma_model import TurmaModel
from appWeb.models.curso_model import CursoModel


class AlunoModel(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField(max_length=50)
    matricula = models.CharField(max_length=20)
    turma = models.ForeignKey(TurmaModel)
    curso = models.ForeignKey(CursoModel)
    nome_pai = models.CharField(max_length=80, blank=True, null=True)
    nome_mae = models.CharField(max_length=80)
    telefone_responsavel = models.CharField(max_length=9)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'