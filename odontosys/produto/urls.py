from django.urls import path
from . import views

app_name = 'produto'
urlpatterns = [
    path('',views.produto_list,name='produto_list'),
    path('<int:pk>',views.produto_details,name='produto_details')
]