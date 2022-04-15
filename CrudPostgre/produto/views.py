from django.shortcuts import render
from .models import * 
from django.views.generic import ListView, DetailView, CreateView, UpdateView,  DeleteView
from django.urls import reverse_lazy



class ProdutoListView(ListView):
    model = Produto
    context_object_name = 'lista_produto'
    template_name = 'produto/produto.html'
    

class ProdutoDetailView(DetailView):
    model = Produto 
    context_object_name = 'produto'
    template_name = 'produto/detalhes.html'
    

class ProdutoCreateView(CreateView):
    model = Produto
    fields = '__all__' # Pega todos os campos. 
    template_name = 'produto/add.html'
    success_url = reverse_lazy('produtos')


class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = '__all__'
    template_name = 'produto/update.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('produtos')


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto/confirme_delete.html'
    success_url = reverse_lazy('produtos')