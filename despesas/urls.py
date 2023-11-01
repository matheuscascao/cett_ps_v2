from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import views_api

router = DefaultRouter()
router.register(r'api/despesas', views_api.DespesaViewSet)
router.register(r'api/categorias', views_api.CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/despesas/<int:pk>/delete/', views_api.DespesaViewSet.as_view({'delete': 'destroy'}), name='despesa-delete'),
    path('api/categorias/<int:pk>/delete/', views_api.CategoriaViewSet.as_view({'delete': 'destroy'}), name='categoria-delete'),

    path('despesas/', views.listar_despesas, name='listar_despesas'),
    path('despesas/filtrar/periodo/', views.filtrar_despesas_periodo, name='filtrar_despesas_periodo'),
    path('despesas/filtrar/categoria/', views.filtrar_despesas_categoria, name='filtrar_despesas_categoria'),
    path('despesas/criar/', views.criar_despesa, name='criar_despesa'),
    path('despesas/editar/<int:despesa_id>/', views.editar_despesa, name='editar_despesa'),
    path('despesas/excluir/<int:despesa_id>/', views.excluir_despesa, name='excluir_despesa'),

    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/criar/', views.criar_categoria, name='criar_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/excluir/<int:categoria_id>/', views.excluir_categoria, name='excluir_categoria'),

]
