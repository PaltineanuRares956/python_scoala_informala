from django import forms
FILTER_CHOICES = [
    ('calorie', 'Calories'),
    ('protein', 'Proteins'),
    ('fat', 'Fats'),
    ('carbohydrate', 'Carbohydrates')
]


class FilterProductForm(forms.Form):
    min_value = forms.IntegerField(required=True,)
    max_value = forms.IntegerField(required=True)
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
