from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import AudioSerializer, CommentSerializer
from .models import Audio, Comment

# Create your views here.

# viewsets provides CRUD implementations
class AudioView(viewsets.ModelViewSet):
    serializer_class = AudioSerializer
    queryset = Audio.objects.all()

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def create(self, request, *args, **kwargs):
        if request.data.get('id'):
            return super(CommentView, self).update(request, *args, **kwargs)
        else:
            return super(CommentView, self).create(request, *args, **kwargs)