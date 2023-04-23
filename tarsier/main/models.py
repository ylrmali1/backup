from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=150, unique=True)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='product', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Blog(models.Model):
    blog_name = models.CharField(max_length=150, unique=True)
    blog_description = models.TextField()
    blog_image = models.ImageField(upload_to='blog', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_name

