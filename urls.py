
from django.urls import path
from . import views

urlpatterns = [

 path('', views.index, name='index'),
 
 path('post/<int:id_post>/', views.post_detalle, name='post_detalle'),
 
 path('estilo/<int:id_estilo>/', views.estilo_detalle, name='estilo_detalle'),
 
 path('interprete/<int:id_interprete>/', views.interprete_detalle, name='interprete_detalle'),
 
 path('cancion/<int:id_cancion>/', views.cancion_detalle, name='cancion_detalle')
]
