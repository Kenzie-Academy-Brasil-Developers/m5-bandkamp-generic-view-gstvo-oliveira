from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import get_object_or_404

from .serializers import SongSerializer
from .models import Song
from albums.models import Album



class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def perform_create(self, serializer):
        album = get_object_or_404( Album, pk=self.kwargs["pk"])
        
        serializer.save(album=album)