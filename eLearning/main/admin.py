from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizAnswer)