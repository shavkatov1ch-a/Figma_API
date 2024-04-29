from django.urls import path
from .views import *

urlpatterns = [
    path('about/', AboutAPIView.as_view(), name='about'),
    path('video/', VideoAPIView.as_view(), name='video'),
    path('gallery/', GalleryAPIView.as_view(), name='gallery'),
    path('trening/', TreningAPIView.as_view(), name='trening'),
    path('author/', AuthorAPIView.as_view(), name='author'),

]