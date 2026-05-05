from django.urls import path
from . import views

app_name = 'produto'
urlpatterns = [
    path('',views.produto_list,name='produto_list'),
    path('<int:pk>',views.produto_details,name='produto_details'),
    path('add/', views.ProdutoCreate.as_view(), name='produto_add'),
    path('<int:pk>/edit/', views.ProdutoUpdate.as_view(), name='produto_edit'),
    path('<int:pk>/alterar/',views.alterar_estoque,name='alterar_estoque'),
    path('<int:pk>/delete',views.produto_delete,name='produto_delete'),
]