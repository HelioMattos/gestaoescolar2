from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView , UpdateView, DeleteView
from .models import Professor

# Create your views here.

class ProfessorListView(ListView):
    model = Professor

class ProfessorCreateView(CreateView):
    model = Professor
    fields = ['nome', 'telefone']
    success_url = reverse_lazy('professor_list')

class ProfessorUpdateView(UpdateView):
    model = Professor
    fields = ['nome', 'telefone']
    success_url = reverse_lazy('professor_list')

class ProfessorDeleteView(DeleteView):
    model = Professor
    success_url = reverse_lazy('professor_list')