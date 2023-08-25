from django.db import models
from ..config.settings import STATIC_ROOT

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()

    thumbnail = models.ImageField(upload_to=STATIC_ROOT, default=(STATIC_ROOT / 'default.png'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)