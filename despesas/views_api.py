from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Despesa, Categoria
from .models import Despesa, Categoria
from .serializers import DespesaSerializer, CategoriaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

    def get_queryset(self):
        print("code reached - queryset")
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
    
    def destroy(self, request, *args, **kwargs):
        print("code reached - destroyed")
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Despesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        print("code reached - queryset")
        queryset = super().get_queryset()
        id_param = self.request.query_params.get('id')

        if id_param:
            queryset = queryset.filter(id=id_param)

        return queryset
    
    def destroy(self, request, *args, **kwargs):
        print("code reached - destroyed")
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Categoria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)