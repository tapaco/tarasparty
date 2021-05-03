from django.shortcuts import render
from rest_framework import generics
from .serealisers import RoomSerializer
from .models import Room

# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer