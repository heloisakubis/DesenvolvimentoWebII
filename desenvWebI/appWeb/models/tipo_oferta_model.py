from django.db import models


class TipoOfertaModel(models.Model):
    nome = models.CharField(max_length=50)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo Oferta'
        verbose_name_plural = 'Tipo Ofertas'