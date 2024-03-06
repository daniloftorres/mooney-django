from django.db import models


class Customer(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = u'Customer'
        verbose_name_plural = u'Customers'
        db_table = 'customer'
