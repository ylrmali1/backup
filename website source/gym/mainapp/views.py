from django.shortcuts import render
from .models import *

# Create your views here.



def home(request):
    context = {
        "text": HomeTexts.objects.all(),
        "carousel": HomeSlayt.objects.all(),
        "photo": HomeSmallPhoto.objects.all(),
    }
    return render(request,'mainapp/home.html',context)

def lessons(request):
    context = {
        "bg": LessonBg.objects.all(),
        "lessons": Lessons.objects.all(),
    }
    return render(request,'mainapp/lessons.html',context)

def about(request):
    context = {
        "bg": AboutBg.objects.all(),
        "description": AboutText.objects.all(),
    }
    return render(request,'mainapp/about.html',context)

def contact(request):
    context = {
        "bg": ContactBg.objects.all(),
        "description": ContactText.objects.all(), 
    }
    return render(request,'mainapp/contact.html',context)


def gallery(request):
    context = {
        "photos": Gallery.objects.all(),
    }
    return render(request,'mainapp/gallery.html',context)

def trainers(request):
    context = {
        "trainers": Trainers.objects.all(),
    }
    return render(request,'mainapp/trainers.html',context)



    