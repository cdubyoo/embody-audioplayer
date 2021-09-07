from django.contrib import admin
from .models import Audio, Comment

class AudioAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'thumbnail')

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'audio', 'user', 'body', 'timestamp_seconds'
    )

# Register your models here.
admin.site.register(Audio, AudioAdmin)
admin.site.register(Comment, CommentAdmin)