from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_perros, name='lista_perros'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('registrar_perro/', views.registrar_perro, name='registrar_perro'),
    path('buscar_usuario/', views.buscar_para_usuario, name='buscar_para_usuario'),
    path('postular/<int:id_perro>/<str:dni_usuario>/', views.postular_adopcion, name='postular_adopcion'),
]