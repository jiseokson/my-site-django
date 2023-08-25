from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()

    thumbnail = models.ImageField(upload_to='static/media/', default='static/media/default.png')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)