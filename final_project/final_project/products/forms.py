from django import forms
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
FILTER_CHOICES = [
    ('calorie', 'Calories'),
    ('protein', 'Proteins'),
    ('fat', 'Fats'),
    ('carbohydrate', 'Carbohydrates')
]


class FilterProductForm(forms.Form):
    min_value = forms.DecimalField(decimal_places=2,
                                   max_digits=4,
                                   min_value=0,
                                   required=False)
    max_value = forms.DecimalField(decimal_places=2,
                                   max_digits=4,
                                   min_value=0,
                                   required=False)
    filter_choice = forms.CharField(widget=forms.RadioSelect(choices=FILTER_CHOICES))


class CaloriesCounterForm(forms.Form):
    product_name = forms.CharField(max_length=50,
                                   required=True)

    quantity = forms.CharField(label='Quantity (g)', widget=forms.NumberInput(attrs={
        'min': 1,
        'max': 10000,
        'type': 'number'
    }),
                               required=True)
