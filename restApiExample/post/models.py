from django.db import models

# Create your models here.


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     username = models.CharField(max_length=20)
#     age = models.IntegerField()
#     city = models.CharField(max_length=50, blank=True, null=True)
#     university = models.CharField(max_length=150, default='Pamukkale University')
#
#     def __str__(self):
#         return self.username


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='posts')
    description = models.CharField(max_length=300, blank=True, null=True)
    # add like and comment after
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['created']
