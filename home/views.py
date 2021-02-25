from django.shortcuts import render
from products.models import Product


# Create your views here.
def index(request):
    """ Products appears on home page order by product name """

    products = Product.objects.all().order_by('-name')
    context = {
        'products': products,
    }
    print(products)
    return render(request, 'home/index.html', context)


