# coding=utf-8
"""Testes de formulário"""
from django.test import TestCase

from appWeb.forms.tipo_oferta_form import TipoOfertaForm
from appWeb.models.tipo_oferta_model import TipoOfertaModel

class TipoOfertaFormTest(TestCase):
    def test_valid_form(self):
        """Método de teste de validação"""

        nome = TipoOfertaModel.objects.create(nome=u'Semestral Teste')

        data = {'nome': nome.nome}

        form = TipoOfertaForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Método de teste de validação com resultado falso"""
        nome = TipoOfertaModel.objects.create(nome=u'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

        data = {'nome': nome.nome}

        form = TipoOfertaForm(data=data)

        self.assertFalse(form.is_valid())