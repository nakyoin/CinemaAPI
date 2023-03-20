from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.forms.models import model_to_dict
from .serializer import *
from rest_framework.generics import *

class FilmApiView(ListCreateAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer


class SingleFilmView(RetrieveUpdateDestroyAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer