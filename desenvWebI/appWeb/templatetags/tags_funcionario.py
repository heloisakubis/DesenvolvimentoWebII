# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django import template

from appWeb.models import AlunoModel
from appWeb.models.funcionario_model import FuncionarioModel

register = template.Library()


@register.filter('verifica_func')
def verifica_func(user, funcao_name):
    """
    Verifica se este usuário pertence a um grupo
    """
    funcao = ''
    try:
        funcao = FuncionarioModel.objects.get(id=user.id).funcao.nome
    except:
        pass
    return True if funcao_name.lower() == funcao.lower() else False


@register.filter('get_aluno')
def get_aluno(url):
    """
    Verifica se este usuário pertence a um grupo
    """
    aluno = []
    try:
        id = int(url.split('/')[3])
        aluno = AlunoModel.objects.get(id=id)
    except:
        pass
    return aluno if aluno else None