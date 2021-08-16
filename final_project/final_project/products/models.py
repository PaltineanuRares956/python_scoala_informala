from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from decimal import Decimal
# Create your models here.


class Product(models.Model):

    class Meta:
        db_table = 'products'

    # TODO:
    # validators for product name!!!!
    name = models.CharField(max_length=50,
                            blank=False,
                            null=False,
                            unique=True,
                            verbose_name='Product name:')
    # TODO:
    # validators for calories
    # calories = models.IntegerField(blank=False,
    #                                max_length=5,
    #                                verbose_name='Calories:')
    # TODO:

    proteins = models.DecimalField(decimal_places=2,
                                   max_digits=4,
                                   validators=[MinValueValidator(Decimal('0.0'), MaxValueValidator(Decimal(100.0)))])

    # TODO:
    fats = models.DecimalField(decimal_places=2,
                               max_digits=4,
                               validators=[MinValueValidator(Decimal('0.0'), MaxValueValidator(Decimal(100.0)))])

    # TODO:
    carbohydrates = models.DecimalField(decimal_places=2,
                                        max_digits=4,
                                        validators=[MinValueValidator(Decimal('0.0'), MaxValueValidator(Decimal(100.0)))])

    calories = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)],
                                   blank=False,
                                   null=False,
                                   default=0)
