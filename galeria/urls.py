from django.urls import path
from galeria.views import index, imagem, buscar_por_nome

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar_por_nome, name="buscar"),
]