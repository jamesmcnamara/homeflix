from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=250)
    path = models.FilePathField(null=False)