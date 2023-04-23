from django.urls import path, include
from quickstart import views
from rest_framework.urlpatterns import format_suffix_patterns
# ViewSet Url
from quickstart.views import SnippetViewSet, UserViewSet
from rest_framework import renderers
# routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]



# actually we don't have to desing the Url conf ourselves.
# Router can design Url Conf for us.
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list',
# })
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = [
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('user/', user_list, name='user-list'),
#     path('user/<int:pk>/', user_detail, name='user-detail'),
#
# ]
#

#
# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
#     path('user/', views.UserList.as_view(), name='user-list'),
#     path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
#
# ]
#
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
#     #path('', views.api_root),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)



