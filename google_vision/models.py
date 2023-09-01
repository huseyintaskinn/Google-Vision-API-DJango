from django.db import models

class GoogleVision(models.Model):
    image = models.ImageField(upload_to='images/')
    result = models.ImageField(upload_to='results/', default="")