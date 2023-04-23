from. import views 
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('lessons',views.lessons, name='lessons'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('gallery',views.gallery, name='gallery'),
]
