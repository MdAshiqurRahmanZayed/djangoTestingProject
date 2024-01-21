from .models import Category

def category_context(request):
     categorys = Category.objects.all()
     return {'categorys':categorys}