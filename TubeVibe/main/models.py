from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import uuid
from django.contrib.auth.models import User


class TimeStamp(models.Model):
     created_at = models.DateTimeField( auto_now_add=True)
     updated_at = models.DateTimeField( auto_now=True)

     class Meta:
          abstract = True

class Category(TimeStamp):
    title = models.CharField( max_length=50)
    slug  = models.SlugField()
     
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.title


class Video(TimeStamp):
     user = models.ForeignKey(User,related_name = "video", on_delete=models.CASCADE)
     title = models.CharField( max_length=100)
     slug  = models.CharField( max_length=100)
     category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name = "video_category")
     youtube_video = models.CharField( max_length=50)
     description = models.TextField(null = True,blank=True)
     
     published = models.BooleanField(default = True)
     
     def save(self, *args, **kwargs):
        video_uuid = uuid.uuid4()
        
        slug_text = f"{self.title}-{video_uuid}"
        self.slug = slugify(slug_text)

        super().save(*args, **kwargs)
        
     def __str__(self):
        return self.title

class Feedback(TimeStamp):
     user = models.ForeignKey(User,related_name = "feedback_user", on_delete=models.CASCADE)
     feedback_video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="feedbacks")
    
     comment = models.TextField()
     
     def __str__(self):
          return f"{self.user.username}'s feedback for {self.feedback_video.title}"