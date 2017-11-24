# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import *

from appWeb.forms.aluno_form import AlunoForm
from appWeb.models.aluno_model import AlunoModel


@method_decorator(login_required, name='dispatch')
class AlunoListView(ListView):
    queryset = AlunoModel.objects.filter(excluido=False).order_by('-id').distinct()
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class AlunoCreateView(CreateView):
    model = AlunoModel
    form_class = AlunoForm
    success_url = '/'


@method_decorator(login_required, name='dispatch')
class AlunoUpdateView(UpdateView):
    model = AlunoModel
    form_class = AlunoForm
    success_url = '/'


@method_decorator(login_required, name='dispatch')
class AlunoDeleteView(DeleteView):
    model = AlunoModel
    success_url = reverse_lazy('aluno_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.excluido = True
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)