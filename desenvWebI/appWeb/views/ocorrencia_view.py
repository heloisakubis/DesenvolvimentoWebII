# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import *

from appWeb.forms import OcorrenciaForm
from appWeb.forms.ocorrencia_form import AlunoSearchForm
from appWeb.models import OcorrenciaModel, FuncionarioModel, AlunoModel


@method_decorator(login_required, name='dispatch')
class OcorrenciaListView(ListView):
    queryset = OcorrenciaModel.objects.filter(excluido=False).order_by('-id').distinct()
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class AlunoOcorrenciaListView(ListView):
    queryset = AlunoModel.objects.filter(excluido=False).order_by('-id').distinct()
    model = AlunoModel
    form_class = AlunoSearchForm
    template_name = 'appWeb/search_alunomodel_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = AlunoModel.objects.filter(excluido=False).order_by('-id').distinct()
        form = self.form_class(self.request.GET)
        if form.is_valid():
            queryset = AlunoModel.objects.filter(nome__icontains=form.cleaned_data['name'], excluido=False).order_by(
                '-id').distinct()
            return queryset
        return queryset



@method_decorator(login_required, name='dispatch')
class OcorrenciaCreateView(CreateView):
    model = OcorrenciaModel
    form_class = OcorrenciaForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.category = get_object_or_404(FuncionarioModel, id=self.request.user.id)
        self.object.save()
        return super(OcorrenciaCreateView, self).form_valid(form)



@method_decorator(login_required, name='dispatch')
class OcorrenciaUpdateView(UpdateView):
    success_url = '/'
    model = OcorrenciaModel
    form_class = OcorrenciaForm



@method_decorator(login_required, name='dispatch')
class OcorrenciaDeleteView(DeleteView):
    model = OcorrenciaModel
    success_url = reverse_lazy('funcionario-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.excluido = True
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)