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
        if 'All' in request.GET:
            return render(request, 'products-list.html', context)
        if 'Filter' in request.GET:
            min_value = int(request.GET.get('min_value'))
            max_value = int(request.GET.get('max_value'))
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
                raise ValueError('Invalid product name')
            quantity = int(request.GET.get('quantity'))

            if not product_exists(product, quantity):
                product_list.append([product, quantity])

            calories, proteins, carbohydrates, fats = get_values()
            context['product_list'] = product_list
            context['total_calories'] = calories
            context['total_proteins'] = proteins
            context['total_carbohydrates'] = carbohydrates
            context['total_fats'] = fats
        elif 'Clear All' in request.GET:
            product_list = []
            context['product_list'] = product_list

    return render(request, 'products-list.html', context)


def product_exists(new_product, new_quantity):

    global product_list
    for index, inner_list in enumerate(product_list):
        product, quantity = inner_list
        if product.name == new_product.name:
            product_list[index] = [product, quantity + new_quantity]
            return True
    return False


def get_values():
    global product_list
    calories, proteins, carbohydrates, fats = 0, 0, 0, 0

    for product, quantity in product_list:
        calories += product.calories * quantity / 100
        proteins += product.proteins * quantity / 100
        carbohydrates += product.carbohydrates * quantity / 100
        fats += product.fats * quantity / 100

    return calories, proteins, carbohydrates, fats
