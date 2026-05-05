from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Produto(models.Model):
    validade = models.DateField(null=False,default=timezone.now)
    ncm = models.CharField('NCM',max_length=8)
    produto = models.CharField(max_length=100)
    preco = models.DecimalField('preço',max_digits=7,decimal_places=2)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque minimo',default=0)

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto
    
    def get_absolute_url(self):
        return reverse('produto:produto_list')
