from django.shortcuts import render
from .models import *
from rest_framework import generics

from .serializers import AboutSerializer, GallerySerializer, TreningSerializer, AuthorSerializer,VideoSerializer


class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class VideoAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class GalleryAPIView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class TreningAPIView(generics.ListAPIView):
    queryset = Trening.objects.all()
    serializer_class = TreningSerializer

class AuthorAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

