# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import *

from appWeb.forms.tipo_funcionario_form import TipoFuncionarioForm
from appWeb.models.tipo_funcionario_model import TipoFuncionarioModel



@method_decorator(login_required, name='dispatch')
class TipoFuncionarioCreateView(CreateView):
    model = TipoFuncionarioModel
    form_class = TipoFuncionarioForm
    success_url = '/'

