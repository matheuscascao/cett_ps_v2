from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Despesa, Categoria
from .forms import DespesaForm, CategoriaForm
from .models import Despesa, Categoria
from .serializers import DespesaSerializer, CategoriaSerializer

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

# class DespesaViewSet(viewsets.ModelViewSet):
#     queryset = Despesa.objects.all()
#     serializer_class = DespesaSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         id_param = self.request.query_params.get('id')
#         categoria_param = self.request.query_params.get('categoria')
#         start_date_param = self.request.query_params.get('start_date')
#         end_date_param = self.request.query_params.get('end_date')

#         if id_param:
#             queryset = queryset.filter(id=id_param)
#         if categoria_param:
#             queryset = queryset.filter(categoria__nome=categoria_param)

#         if start_date_param and end_date_param:
#             queryset = queryset.filter(data__range=(start_date_param, end_date_param))

#         return queryset

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer