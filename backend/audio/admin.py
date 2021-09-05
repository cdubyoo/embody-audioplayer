from django.contrib import admin
from .models import Audio

class AudioAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'thumbnail')

# Register your models here.
admin.site.register(Audio, AudioAdmin)