from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Quarto, Reserva, Funcionario, Pagamento


# HOME
def home(request):
    context = {
        'quartos': Quarto.objects.all(),
        'clientes': Cliente.objects.all(),
        'reservas': Reserva.objects.all(),
    }
    return render(request, 'home.html', context)


# =========================
# QUARTO
# =========================

class QuartoListView(ListView):
    model = Quarto
    template_name = 'quarto_list.html'


class QuartoCreateView(CreateView):
    model = Quarto
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class QuartoUpdateView(UpdateView):
    model = Quarto
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class QuartoDeleteView(DeleteView):
    model = Quarto
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')


# =========================
# CLIENTE
# =========================

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'


class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')


# =========================
# RESERVA
# =========================

class ReservaListView(ListView):
    model = Reserva
    template_name = 'reserva_list.html'


class ReservaCreateView(CreateView):
    model = Reserva
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')


# =========================
# FUNCIONARIO
# =========================

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'funcionario_list.html'


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')


# =========================
# PAGAMENTO
# =========================

class PagamentoListView(ListView):
    model = Pagamento
    template_name = 'pagamento_list.html'


class PagamentoCreateView(CreateView):
    model = Pagamento
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class PagamentoUpdateView(UpdateView):
    model = Pagamento
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class PagamentoDeleteView(DeleteView):
    model = Pagamento
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')