from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/<int:pk>', views.blog_detail, name='blog_detail'),
]