from rest_framework import serializers
from .models import Audio, Comment

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        # things that need to be converted to JSON
        fields = ('id','artist', 'title', 'thumbnail') 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'audio', 'user', 'body', 'timestamp_minutes', 'timestamp_seconds') 