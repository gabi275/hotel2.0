from django.db import models

class Quarto(models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Quarto {self.numero}"


class Reserva(models.Model):
    nome_cliente = models.CharField(max_length=100)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    data_entrada = models.DateField()
    data_saida = models.DateField()

    def __str__(self):
        return self.nome_cliente
