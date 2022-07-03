from django.db import models

# Create your models here.

class Image(models.Model):
    Image = models.ImageField(upload_to='mypic')
    Date = models.DateTimeField(auto_now_add=True)