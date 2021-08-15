from django.shortcuts import render, reverse
from .models import Product
from django.http import HttpResponseRedirect

# Create your views here.


def products_view(request):

    if request.POST:
        print('123')
        if 'Products' in request.POST:
            print('12')
            return HttpResponseRedirect(reverse('products-list'))

    return render(request, 'products.html', {})


def products_list_view(request):
    queryset = Product.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'products-list.html', context)