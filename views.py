from django.views import View
from django.shortcuts import get_list_or_404, get_object_or_404
from myapp.models import Estilo
from myapp.models import Interprete
from myapp.models import Cancion


def index(request):
 elementos_list = Estilo.objects.all()
 canciones = Cancion.objects.all().order_by('popularidad')[:100]
 context = {'elementos' : elementos_list, "canciones" : canciones}
 return render(request, 'myapp/index.html', context)
 
def cancion_detalle(request, id_cancion):
 cancion = Cancion.objects.get(id = id_cancion)
 interpretes = cancion.interprete.all()
 estilo = Estilo.objects.get(nombre = cancion.estilo)
 context = {"cancion" : cancion, "interpretes" : interpretes, "estilo" : estilo}
 
 return render(request, 'myapp/cancion.html', context)
 
def estilo_detalle(request, id_estilo):
 estilo = Estilo.objects.get(id = id_estilo)
 cancion_list = Cancion.objects.all()
 context = {"estilo" : estilo, "canciones" : cancion_list}
 
 return render(request, 'myapp/estilo.html', context)
 
def interprete_detalle(request, id_interprete):
 interprete = Interprete.objects.get(id = id_interprete)
 interpretes = interprete.cancion_set.all()
 context = {"interprete" : interprete, "interpretes" : interpretes} 
 
 return render(request, 'myapp/interprete.html', context)
