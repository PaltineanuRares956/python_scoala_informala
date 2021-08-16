from django.shortcuts import render, reverse
from .models import Product
from django.http import HttpResponseRedirect
from .forms import FilterProductForm
# Create your views here.


def products_view(request):

    if request.POST:
        if 'Products' in request.POST:
            return HttpResponseRedirect(reverse('products-list'))

    return render(request, 'products.html', {})


def products_list_view(request):
    form = FilterProductForm()
    queryset = Product.objects.all()
    context = {
        'form': form,
        'queryset': queryset
    }

    if request.GET:
        if 'All' not in request.GET:
            min_value = request.GET.get('min_value')
            max_value = request.GET.get('max_value')
            filter_choice = request.GET.get('filter_choice')
            if min_value > max_value:
                print(min_value)
                print(max_value)
                context['invalid'] = True
            else:
                if context.get('invalid'):
                    print('123')
                    context.pop('invalid')
                if filter_choice == 'protein':
                    queryset = Product.objects.filter(proteins__gte=min_value, proteins__lte=max_value)
                elif filter_choice == 'fat':
                    queryset = Product.objects.filter(fats__gte=min_value, fats__lte=max_value)
                elif filter_choice == 'carbohydrate':
                    queryset = Product.objects.filter(carbohydrates__gte=min_value, carbohydrates__lte=max_value)
                elif filter_choice == 'calorie':
                    queryset = Product.objects.filter(calories__gte=min_value, calories__lte=max_value)
                context['queryset'] = queryset

    return render(request, 'products-list.html', context)
