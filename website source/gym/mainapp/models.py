from asyncio.windows_events import NULL
from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Lessons(models.Model):
    image = models.ImageField(upload_to="lessons")
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=150,null=True,blank=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title}"

class LessonBg(models.Model):        
    background_image= models.ImageField(upload_to="lessons")

class HomeSlayt(models.Model):
    file = models.FileField(upload_to='homepage')
    
class HomeSmallPhoto(models.Model):
    image1 = models.ImageField(upload_to='homepage')
    image2 = models.ImageField(upload_to='homepage')

class AboutText(models.Model):
    description = models.TextField()

class AboutBg(models.Model):
    background_image= models.ImageField(upload_to="about")

class ContactBg(models.Model):
    background_image= models.ImageField(upload_to="contact")

class ContactText(models.Model):
    description = models.TextField()

class Trainers(models.Model):
    image = models.ImageField(upload_to="trainers",null=True,blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200,null=True,blank=True)
    age = models.CharField(max_length=2,null=True,blank=True)
    major = models.CharField(max_length=100,null=True,blank=True)
    number = models.CharField(max_length=11,null=True,blank=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"
    
class HomeTexts(models.Model):
    text1 = models.CharField(max_length=150)
    text2 = models.CharField(max_length=150)
    text3 = models.CharField(max_length=150)
    text4 = models.CharField(max_length=150)
    def __str__(self):
        return f"Home Text"
    
class Gallery(models.Model):
    photo = models.ImageField(upload_to='uploads',null=True,blank=True)
    photo2 = models.ImageField(upload_to='uploads',null=True,blank=True)


    
