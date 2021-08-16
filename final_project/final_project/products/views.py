from django.shortcuts import render, reverse
from .models import Product
from django.http import HttpResponseRedirect
from .forms import FilterProductForm, CaloriesCounterForm
# Create your views here.


def products_view(request):

    if request.POST:
        if 'Products' in request.POST:
            return HttpResponseRedirect(reverse('products-list'))

    return render(request, 'products.html', {})


product_list = []


def products_list_view(request):
    form = FilterProductForm()
    form_calories = CaloriesCounterForm()
    queryset = Product.objects.all()
    context = {
        'form': form,
        'form_calories': form_calories,
        'queryset': queryset
    }
    global product_list
    if request.GET:
        if 'All' not in request.GET:
            if 'Filter' in request.GET:
                min_value = request.GET.get('min_value')
                max_value = request.GET.get('max_value')
                filter_choice = request.GET.get('filter_choice')
                if min_value > max_value:
                    context['invalid_values'] = True
                else:
                    if context.get('invalid_values'):
                        context.pop('invalid_values')
                    if filter_choice == 'protein':
                        queryset = Product.objects.filter(proteins__gte=min_value, proteins__lte=max_value)
                    elif filter_choice == 'fat':
                        queryset = Product.objects.filter(fats__gte=min_value, fats__lte=max_value)
                    elif filter_choice == 'carbohydrate':
                        queryset = Product.objects.filter(carbohydrates__gte=min_value, carbohydrates__lte=max_value)
                    elif filter_choice == 'calorie':
                        queryset = Product.objects.filter(calories__gte=min_value, calories__lte=max_value)
                    context['queryset'] = queryset
            elif 'Add' in request.GET:
                try:
                    product = Product.objects.get(name=request.GET.get('product_name'))
                except Product.DoesNotExist:
                    context['invalid_product_name'] = True
                    raise ValueError('Invalid product name')

                if context.get('invalid_product_name'):
                    context.pop('invalid_product_name')
                quantity = request.GET.get('quantity')
                product_list.append((product, quantity))
                context['product_list'] = product_list

    return render(request, 'products-list.html', context)
