# -*- coding: utf-8 -*-
from django.db import models

from appWeb.models.aluno_model import AlunoModel
from appWeb.models.funcionario_model import FuncionarioModel
from appWeb.models.tipo_permissao_model import TipoPermissaoModel


class PermissaoModel(models.Model):
    aluno = models.ForeignKey(AlunoModel, null=True, blank=True, related_name='_aluno_',
                              verbose_name='Aluno')
    matricula_aluno = models.ForeignKey(AlunoModel, null=True, blank=True, related_name='_matricula_aluno_',
                              verbose_name='Matricula Aluno')
    turma_aluno = models.ForeignKey(AlunoModel, null=True, blank=True, related_name='_turma_aluno_',
                              verbose_name='Turma Aluno')
    curso_aluno = models.ForeignKey(AlunoModel, null=True, blank=True, related_name='_curso_aluno_',
                              verbose_name='Curso Aluno')
    tipo_permissao = models.ForeignKey(TipoPermissaoModel)
    data = models.DateTimeField()
    motivo = models.TextField(max_length=150)
    funcionario = models.ForeignKey(FuncionarioModel)


    def __unicode__(self):
        return self.aluno

    def __str__(self):
        return self.aluno

    class Meta:
        verbose_name = 'Permissao'
        verbose_name_plural = 'Permissoes'