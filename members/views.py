from django.shortcuts import render
from .models import Product

def members_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'members/index.html', context)