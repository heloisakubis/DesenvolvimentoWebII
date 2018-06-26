# coding=utf-8

from django.test import TestCase
from appWeb.models.tipo_oferta_model import TipoOfertaModel


class TipoOfertaModelTest(TestCase):
    """Classe de teste da model Tipo Oferta"""
    def create_oferta(self, nome=u'Semestral Teste'):
        """Método cria tipo oferta"""
        return TipoOfertaModel.objects.create(nome=nome)

    def teste_tipo_oferta_criacao(self):
        """Testa a criação de tipo oferta"""
        nome = self.create_oferta()
        self.assertTrue(isinstance(nome, TipoOfertaModel))
        self.assertEqual(nome.__unicode__(), nome.nome)
