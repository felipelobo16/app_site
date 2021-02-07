from django.shortcuts import render, redirect
from app.models import Produtos
from app.forms import ProdutoForm


# Create your views here.
def home(r):
    db = Produtos.objects.all()
    return render(r, 'index.html/', {'db': db})

def form(r):
    form = ProdutoForm()
    return render(r, 'cadastro.html/', {'form': form})

def view(r,pk):
    db = Produtos.objects.get(pk=pk)
    return render(r, 'view.html', {'db':db})

def criar(r):
    form = ProdutoForm(r.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def editar(r, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutoForm(instance=data['db'])
    return render(r, 'cadastro.html', data)

def update(r, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    form = ProdutoForm(r.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def deletar(r,pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('home')