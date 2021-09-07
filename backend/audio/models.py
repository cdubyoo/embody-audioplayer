from django.db import models

# Create your models here.
class Audio(models.Model):
    artist = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    thumbnail = models.ImageField()

    def _str_(self):
        return self.title + ' - ' + self.artist

class Comment(models.Model):
    audio = models.ForeignKey(Audio, related_name='comment', on_delete=models.CASCADE)
    user = models.CharField(max_length=16)
    body =  models.TextField()
    timestamp_seconds = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']

    def _str_ (self):
        return 'Comment {} by {} at {}:{}'.format(
            self.body, self.user, self.timestamp_minutes, self.timestamp_seconds
        )