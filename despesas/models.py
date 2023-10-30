from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Despesa(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.descricao
