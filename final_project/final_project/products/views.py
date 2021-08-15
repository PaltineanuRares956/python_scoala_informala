from django.shortcuts import render, reverse
from .models import Product
from django.http import HttpResponseRedirect
from .forms import FilterProductForm
# Create your views here.


def products_view(request):

    if request.POST:
        print('123')
        if 'Products' in request.POST:
            print('12')
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
        #if request.GET.get('min_value') != '' and request.GET.get('max_value') != '':
        if 'All' not in request.GET:
            min_value = request.GET.get('min_value')
            max_value = request.GET.get('max_value')
            filter_choice = request.GET.get('filter_choice')
            if min_value > max_value:
                context['invalid'] = True
            else:
                if filter_choice == 'protein':
                    queryset = Product.objects.filter(proteins__gte=min_value, proteins__lte=max_value)
                elif filter_choice == 'fat':
                    queryset = Product.objects.filter(fats__gte=min_value, fats__lte=max_value)
                elif filter_choice == 'carbohydrate':
                    queryset = Product.objects.filter(carbohydrates__gte=min_value, carbohydrates__lte=max_value)
                context['queryset'] = queryset
    # if request.GET:
    #    print('123')
    #    print(request.GET)
    #    if 'Min' and 'Max' in request.GET:
    #        min_value = request.GET.get('Min')
    #        max_value = request.GET.get('Max')
#
    #        if 'Proteins' in request.GET:
    #            context['proteins'] = True
    #        if 'Fats' in request.GET:
    #            context['fats'] = True
    #        if 'Carbohydrates' in request.GET:
    #            context['carbohydrates'] = True


    return render(request, 'products-list.html', context)
