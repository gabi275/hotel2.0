from django.urls import path
from .views import *

urlpatterns = [

    path('', home, name='home'),

    # QUARTOS
    path('quartos/', QuartoListView.as_view(), name='quarto_list'),
    path('quartos/novo/', QuartoCreateView.as_view(), name='quarto_create'),
    path('quartos/editar/<int:pk>/', QuartoUpdateView.as_view(), name='quarto_update'),
    path('quartos/excluir/<int:pk>/', QuartoDeleteView.as_view(), name='quarto_delete'),

    # CLIENTES
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/novo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/excluir/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # RESERVAS
    path('reservas/', ReservaListView.as_view(), name='reserva_list'),
    path('reservas/novo/', ReservaCreateView.as_view(), name='reserva_create'),
    path('reservas/editar/<int:pk>/', ReservaUpdateView.as_view(), name='reserva_update'),
    path('reservas/excluir/<int:pk>/', ReservaDeleteView.as_view(), name='reserva_delete'),

        # FUNCIONARIOS
    path('funcionarios/', FuncionarioListView.as_view(), name='funcionario_list'),
    path('funcionarios/novo/', FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('funcionarios/editar/<int:pk>/', FuncionarioUpdateView.as_view(), name='funcionario_update'),
    path('funcionarios/excluir/<int:pk>/', FuncionarioDeleteView.as_view(), name='funcionario_delete'),

    # PAGAMENTOS
    path('pagamentos/', PagamentoListView.as_view(), name='pagamento_list'),
    path('pagamentos/novo/', PagamentoCreateView.as_view(), name='pagamento_create'),
    path('pagamentos/editar/<int:pk>/', PagamentoUpdateView.as_view(), name='pagamento_update'),
    path('pagamentos/excluir/<int:pk>/', PagamentoDeleteView.as_view(), name='pagamento_delete'),
]