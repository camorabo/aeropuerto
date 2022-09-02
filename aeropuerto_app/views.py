from django.shortcuts import render
from aeropuerto_app.models import *
from aeropuerto_app.serializers import *
from rest_framework import viewsets,status
# Create your views here.
# Es como la capa del controlador.

class Avion_view(viewsets.ModelViewSet):
    # Para hacer peticiones queryset
    queryset = Avion.objects.all()
    # El serializador que vamos a tener.
    serializer_class = Avion_Serializer