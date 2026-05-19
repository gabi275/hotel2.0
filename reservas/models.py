from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Quarto(models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Quarto {self.numero}"


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    data_entrada = models.DateField()
    data_saida = models.DateField()

    def __str__(self):
        return str(self.cliente)


class Pagamento(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    metodo = models.CharField(max_length=50)

    def __str__(self):
        return self.metodo
