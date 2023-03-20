from rest_framework import serializers
from rest_framework.response import Response

from .models import *

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'
