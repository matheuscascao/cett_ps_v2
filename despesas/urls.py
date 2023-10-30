from django.urls import path
from . import views

urlpatterns = [
    path('despesas/', views.listar_despesas, name='listar_despesas'),
    path('despesas/criar/', views.criar_despesa, name='criar_despesa'),
    path('despesas/editar/<int:despesa_id>/', views.editar_despesa, name='editar_despesa'),
    path('despesas/excluir/<int:despesa_id>/', views.excluir_despesa, name='excluir_despesa'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/criar/', views.criar_categoria, name='criar_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/excluir/<int:categoria_id>/', views.excluir_categoria, name='excluir_categoria'),
]