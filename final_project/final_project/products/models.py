from django.db import models

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
                                   max_digits=2)

    # TODO:
    fats = models.DecimalField(decimal_places=2,
                               max_digits=2)

    # TODO:
    carbohydrates = models.DecimalField(decimal_places=2,
                                        max_digits=2)