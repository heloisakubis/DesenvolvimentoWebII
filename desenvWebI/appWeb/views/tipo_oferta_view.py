# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import *
from appWeb.forms import TipoOfertaForm
from appWeb.models import TipoOfertaModel


@method_decorator(login_required, name='dispatch')
class TipoOfertaCreateView(CreateView):
    model = TipoOfertaModel
    form_class = TipoOfertaForm
    success_url = '/'