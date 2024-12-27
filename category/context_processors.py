from .models import Category

# to generate the URL for each category.
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)