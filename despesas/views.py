from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Despesa, Categoria
from .forms import DespesaForm, CategoriaForm
from .models import Despesa, Categoria

def listar_despesas(request):
    despesas = Despesa.objects.all()
    return render(request, 'despesas/listar_despesas.html', {'despesas': despesas})

def filtrar_despesas_periodo(request): 
    data_inicio = request.GET.get('data_inicio', None)
    data_fim = request.GET.get('data_fim', None)

    # Optionally, you can validate the date inputs here.

    if data_inicio and data_fim:
        despesas = Despesa.objects.filter(data__range=[data_inicio, data_fim])
    else:
        despesas = Despesa.objects.all()

    return render(request, 'despesas/filtrar_despesas_periodo.html', {'despesas': despesas})

def filtrar_despesas_categoria(request):
    categoria_nome = request.GET.get('categoria_nome', None)

    if categoria_nome:
        despesas = Despesa.objects.filter(categorias__nome=categoria_nome)
    else:
        despesas = Despesa.objects.all()

    return render(request, 'despesas/filtrar_despesas_categoria.html', {'despesas': despesas})



def criar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_despesas')
    else:
        form = DespesaForm()
    return render(request, 'despesas/criar_despesa.html', {'form': form})

def editar_despesa(request, despesa_id):
    despesa = Despesa.objects.get(id=despesa_id)
    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return redirect('listar_despesas')
    else:
        form = DespesaForm(instance=despesa)
    return render(request, 'despesas/editar_despesa.html', {'form': form, 'despesa': despesa})

def excluir_despesa(request, despesa_id):
    despesa = Despesa.objects.get(id=despesa_id)
    despesa.delete()
    return redirect('listar_despesas')

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar_categorias.html', {'categorias': categorias})

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/criar_categoria.html', {'form': form})

def editar_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/editar_categoria.html', {'form': form, 'categoria': categoria})

def excluir_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    categoria.delete()
    return redirect('listar_categorias')