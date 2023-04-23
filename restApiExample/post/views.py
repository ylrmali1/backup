from django.shortcuts import render
from .request import Api

# Create your views here.


def users(request):
    name = Api().get_users()
    post = Api().get_posts()
    context = {
        'users': name,
    }
    return render(request, 'users.html', context)
