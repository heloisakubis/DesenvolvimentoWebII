# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from appWeb.models import OcorrenciaModel



@method_decorator(login_required, name='dispatch')
class IndexListView(ListView):
    queryset = OcorrenciaModel.objects.filter(excluido=False).order_by('-id').distinct()
    paginate_by = 10
    template_name = 'index.html'