from django.urls import path, include
from post.api import views as api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', api_views.PostViewSet, basename='post')
router.register(r'users', api_views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
