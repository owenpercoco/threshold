from .models import Category

def data_for_categories(request):
    CATEGORIES = Category.objects.all()

    return {'CATEGORIES': CATEGORIES}