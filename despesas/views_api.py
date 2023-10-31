from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Despesa, Categoria
from .forms import DespesaForm, CategoriaForm
from .models import Despesa, Categoria
from .serializers import DespesaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        id_param = self.request.query_params.get('id')
        categoria_param = self.request.query_params.get('categoria')
        start_date_param = self.request.query_params.get('start_date')
        end_date_param = self.request.query_params.get('end_date')

        if id_param:
            queryset = queryset.filter(id=id_param)
        if categoria_param:
            queryset = queryset.filter(categoria__nome=categoria_param)

        if start_date_param and end_date_param:
            queryset = queryset.filter(data__range=(start_date_param, end_date_param))

        return queryset