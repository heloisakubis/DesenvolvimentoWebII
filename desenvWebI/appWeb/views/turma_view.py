# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import *
from appWeb.forms import TurmaForm
from appWeb.models import TurmaModel


@method_decorator(login_required, name='dispatch')
class TurmaListView(ListView):
    queryset = TurmaModel.objects.filter(excluido=False).order_by('-id').distinct()
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class TurmaCreateView(CreateView):
    model = TurmaModel
    form_class = TurmaForm
    success_url = '/'


@method_decorator(login_required, name='dispatch')
class TurmaUpdateView(UpdateView):
    model = TurmaModel
    form_class = TurmaForm
    success_url = '/'


@method_decorator(login_required, name='dispatch')
class TurmaDeleteView(DeleteView):
    model = TurmaModel
    success_url = reverse_lazy('turma_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.excluido = True
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)