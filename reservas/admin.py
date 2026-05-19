from django.contrib import admin
from .models import Cliente, Quarto, Funcionario, Reserva, Pagamento

admin.site.register(Cliente)
admin.site.register(Quarto)
admin.site.register(Funcionario)
admin.site.register(Reserva)
admin.site.register(Pagamento)