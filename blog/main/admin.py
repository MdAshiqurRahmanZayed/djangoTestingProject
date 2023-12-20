from django.contrib import admin
from main.models import Blog, Comment, Like

class CustomBlog(admin.ModelAdmin):
     model = Blog
     prepopulated_fields = {
          "slug":('blog_title',)
     }

admin.site.register(Blog,CustomBlog)
admin.site.register(Comment)
admin.site.register(Like)
