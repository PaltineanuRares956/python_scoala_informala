from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from decimal import Decimal
# Create your models here.


class Product(models.Model):

    class Meta:
        db_table = 'products'

    name = models.CharField(max_length=50,
                            blank=False,
                            null=False,
                            unique=True,
                            verbose_name='Product name:')

    proteins = models.DecimalField(decimal_places=2,
                                   max_digits=4,
                                   validators=[MinValueValidator(Decimal('0.0'), MaxValueValidator(Decimal(100.0)))])

    fats = models.DecimalField(decimal_places=2,
                               max_digits=4,
                               validators=[MinValueValidator(Decimal('0.0'), MaxValueValidator(Decimal(100.0)))])

    carbohydrates = models.DecimalField(decimal_places=2,
                                        max_digits=4,
                                        validators=[MinValueValidator(Decimal('0.0'), MaxValueValidator(Decimal(100.0)))])

    calories = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)],
                                   blank=False,
                                   null=False,
                                   default=0)

    def clean(self):
        if name_has_numbers(self.name):
            raise ValidationError('Invalid name')
        if self.proteins + self.carbohydrates + self.fats > 100:
            raise ValidationError('The sum of the macronutrients is bigger than 100!')


def name_has_numbers(name):
    return any(ch.isdigit() for ch in name)
