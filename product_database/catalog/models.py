from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):

    name = models.CharField(max_length=200, help_text="Enter a product name")
    favorite = models.ManyToManyField(User, blank=True, related_name='favorite_type')
    who_added = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_added_to_product_type')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('product-detail', args=[str(self.id)])


class Store(models.Model):

    name = models.CharField(max_length=50, help_text="Enter a store name")
    location = models.CharField(max_length=100, help_text="Enter store location")
    who_added = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_added_to_store_type')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('store-detail', args=[str(self.id)])


class Price(models.Model):

    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    who_added = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_added_to_price_type')

    def __str__(self):
        return self.product.name


UNITS = (
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
        ('thing', 'Thing')
    )


class ProductAmount(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    unit = models.CharField(max_length=10, choices=UNITS, default='k', help_text='Choose unit')
    related_model = models.ForeignKey('Dish', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class KitchenUtensil(models.Model):

    name = models.CharField(max_length=100, help_text='Enter kitchen utensil name')
    who_added = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_added_to_kitchen_utensil_type', null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):

    name = models.CharField(max_length=200)
    recipe = models.CharField(max_length=100000)
    kitchen_utensils = models.ManyToManyField('KitchenUtensil', blank=False)
    products = models.ManyToManyField('ProductAmount', blank=True)
    who_added = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_added_to_dish_type', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('dish-detail', args=[str(self.id)])
