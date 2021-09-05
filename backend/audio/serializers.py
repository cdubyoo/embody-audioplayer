from rest_framework import serializers
from .models import Audio

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        # things that need to be converted to JSON
        fields = ('artist', 'title', 'thumbnail') 