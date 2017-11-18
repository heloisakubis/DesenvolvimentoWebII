# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView


def index(request):
    context={}
    template_name= 'index_professor.html'
    return render(request, template_name, context)

# class Alunos(ListView):
#     queryset = Alunos.objects.all().exclude(excluido=True)
#     template_name = 'alunos.html'
#
# class Cursos(ListView):
#     queryset = Cursos.objects.all().exclude(excluido=True)
#     template_name = 'cursos.html'
#
# class Funcionarios(ListView):
#     queryset = Funcionarios.objects.all().exclude(excluido=True)
#     template_name = 'funcionarios.html'
#
# class Permissoes(ListView):
#     queryset = Permissoes.objects.all().exclude(excluido=True)
#     template_name = 'permissoes.html'
#
# class Turmas(ListView):
#     queryset = Turmas.objects.all().exclude(excluido=True)
#     template_name = 'turmas.html'