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
    context = {}
    if request.GET:
        print('123')
        print(request.GET)
        if 'Min' and 'Max' in request.GET:
            min_value = request.GET.get('Min')
            max_value = request.GET.get('Max')

            if 'Proteins' in request.GET:
                context['proteins'] = True
            if 'Fats' in request.GET:
                context['fats'] = True
            if 'Carbohydrates' in request.GET:
                context['carbohydrates'] = True


    return render(request, 'products-list.html', context)
