from django import forms

FILTER_CHOICES = [
    ('protein', 'Proteins'),
    ('fat', 'Fats'),
    ('carbohydrate', 'Carbohydrates')
]


class FilterProductForm(forms.Form):
    min_value = forms.DecimalField(decimal_places=2,
                                   max_digits=4,
                                   min_value=0,
                                   max_value=100,
                                   required=False)
    max_value = forms.DecimalField(decimal_places=2,
                                   max_digits=4,
                                   min_value=0,
                                   max_value=100,
                                   required=False)
    filter_choice = forms.CharField(widget=forms.RadioSelect(choices=FILTER_CHOICES))
