from django.db import models


class TipoOfertaModel(models.Model):
    descricao = models.CharField(max_length=50)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Tipo Oferta'
        verbose_name_plural = 'Tipo Ofertas'