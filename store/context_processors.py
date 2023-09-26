from .models import Category


# Write the Context Processors
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return context