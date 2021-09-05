from django.db import models

# Create your models here.
class Audio(models.Model):
    artist = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    thumbnail = models.ImageField()

    def _str_(self):
        return self.title