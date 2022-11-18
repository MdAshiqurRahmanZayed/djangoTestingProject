from email.policy import default
from time import timezone
from turtle import title
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class BookStore(models.Model):
     title = models.CharField( max_length = 100 )
     author = models.CharField( max_length = 50 )
     descriptions = models.TextField()
     date_created = models.DateTimeField(default = timezone.now)
     
     slug = models.SlugField()
    

     class Meta:
          verbose_name = ("BookStore")
          verbose_name_plural = ("BookStores")

     def __str__(self):
          return self.title
     
     def save(self,*args, **kwargs):
          self.slug = slugify(self.title)
          super().save(*args, **kwargs)

