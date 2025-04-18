from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Gestao

# Create your views here.

class GestaoListView(ListView):
    model = Gestao

class GestaoCreateView(CreateView):
    model = Gestao
    fields = ['disciplina']
    success_url = reverse_lazy('gestao_list')

class GestaoUpdateview(UpdateView):
    model = Gestao
    fields = ['disciplina']
    success_url = reverse_lazy('gestao_list')

class GestaoDeleteView(DeleteView):
    model = Gestao
    fields = ['disciplina']
    success_url = reverse_lazy('gestao_list')
    

