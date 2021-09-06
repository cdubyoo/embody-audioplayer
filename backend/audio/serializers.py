from rest_framework import serializers
from .models import Audio, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'audio', 'user', 'body', 'timestamp_minutes', 'timestamp_seconds') 
    
class AudioSerializer(serializers.ModelSerializer):
    # associating comments with audio
    comment = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='body'
     )

    class Meta:
        model = Audio
        # things that need to be converted to JSON
        fields = ('id','artist', 'title', 'thumbnail', 'comment') 

