from django.db import models

class UploadedZip(models.Model):
    zip_file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name