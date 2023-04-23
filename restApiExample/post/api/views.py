from rest_framework import viewsets
from post.api.serializers import UserSerializer, PostSerializer
from post.models import Post
from django.contrib.auth.models import User
from rest_framework import permissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # list, retrieve
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    # list, create, retrieve, update, destroy
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
