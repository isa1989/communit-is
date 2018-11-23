from django.db import models
import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class About(models.Model):
    title_a = models.CharField(max_length=100)
    content_a = models.TextField()
    #title_a = RichTextField()
    content_a = RichTextField()

    def __str__(self):
        return self.title_a


class Services(models.Model):
    title_s = models.CharField(max_length=100)
    content_s = models.TextField()
    image = models.ImageField()
    content_s = RichTextField()
    def __str__(self):
        return self.title_s


