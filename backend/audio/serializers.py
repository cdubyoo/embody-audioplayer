from rest_framework import serializers
from .models import Audio, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'audio', 'user', 'body','timestamp_seconds') 
    
class AudioSerializer(serializers.ModelSerializer):
    # associating comments with audio
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Audio
        # things that need to be converted to JSON
        fields = '__all__'

    def get_comments(self, obj):
        return CommentSerializer(obj.comment.all(), many=True).data


