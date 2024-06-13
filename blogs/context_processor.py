from blogs.models import Category


def categories_processor(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return context
