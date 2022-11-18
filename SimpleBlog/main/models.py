from enum import unique
from time import timezone
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

class Blog(models.Model):
     title = models.CharField( unique=True, max_length = 50 )
     author = models.CharField( max_length = 50 )
     descriptions = models.TextField()
     image =   models.ImageField(null=False,blank=True,upload_to="images/")
     date_created = models.DateTimeField(default = timezone.now)

     slug = models.SlugField()




     class Meta:
          verbose_name = ("Blog")
          verbose_name_plural = ("Blogs")

     def __str__(self):
          return self.title
     
     def save(self,*args, **kwargs):
          self.slug = slugify(self.title)
          super().save(*args, **kwargs)



