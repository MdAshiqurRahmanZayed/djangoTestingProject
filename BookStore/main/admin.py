from django.contrib import admin
from .models import BookStore
# Register your models here.
class BookStoreAdmin(admin.ModelAdmin):
     prepopulated_fields = {
          "slug" :("title",)
     }


admin.site.register(BookStore,BookStoreAdmin)