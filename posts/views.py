from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.serializers import PostSerializer

class PostViweSet(ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer