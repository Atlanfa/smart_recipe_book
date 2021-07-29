from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from .choices import CPAS, UNITS, SEXES
from location_field.models.plain import PlainLocationField


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEXES, default='m')
    weight = models.FloatField(null=True)
    nursing = models.BooleanField(blank=True, null=True)
    cpa = models.CharField(max_length=3, choices=CPAS, default='i')
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    location = PlainLocationField(based_fields=['country', 'city'], zoom=7, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Product(models.Model):

    name = models.CharField(max_length=200, help_text="Enter a product name")
    favorite = models.ManyToManyField(User, blank=True, related_name='favorite_product_type')
    who_added = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_added_to_product_type')
    proteins_in_100_g = models.FloatField()
    proteins_in_100_g_including_animals = models.FloatField()
    fat_in_100_g = models.FloatField()
    fat_in_100_g_including_animals = models.FloatField()
    digestible_carbohydrates_in_100_g = models.FloatField()
    digestible_carbohydrates_in_100_g_incl_m_and_d = models.FloatField()
    dietary_fiber_in_100_g = models.FloatField()
    dietary_fiber_in_100_g_including_fiber_and_pectin = models.FloatField()
    polyunsaturated_acid = models.FloatField()
    saturated_acid = models.FloatField()
    monounsaturated_acid = models.FloatField()
    calcium_in_100_g_in_mg = models.FloatField()
    phosphorus_in_100_g_in_mg = models.FloatField()
    magnesium_in_100_g_in_mg = models.FloatField()
    potassium_in_100_g_in_mg = models.FloatField()
    sodium_in_100_g_in_mg = models.FloatField()
    chlorine_in_100_g_in_mg = models.FloatField()
    sulfur_in_100_g_in_mg = models.FloatField()
    iron_in_100_g_in_mg = models.FloatField()
    zinc_in_100_g_in_mg = models.FloatField()
    iodine_in_100_g_in_mg = models.FloatField()
    fluorine_in_100_g_in_mg = models.FloatField()
    thiamine_vitamin_B1_in_100_g_in_mg = models.FloatField()
    riboflavin_vitamin_B2_in_100_g_in_mg = models.FloatField()
    pyridoxine_vitamin_B6_in_100_g_in_mg = models.FloatField()
    pantothenic_acid_vitamin_B3_in_100_g_in_mg = models.FloatField()
    folacin_acid_vitamin_B9_in_100_g_in_mcg = models.FloatField()
    cobalamin_acid_vitamin_B12_in_100_g_in_mcg = models.FloatField()
    niacin_vitamin_PP_in_100_g_in_mg = models.FloatField()
    ascorbic_acid_vitamin_C_in_100_g_in_mg = models.FloatField()
    retinol_vitamin_A_in_100_g_in_mcg = models.FloatField()
    tocopherol_vitamin_E_in_100_g_in_mg = models.FloatField()
    cholecalciferol_vitamin_D_in_100_g_in_mcg = models.FloatField()
    energy_value_in_kcal = models.FloatField()

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
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    location = PlainLocationField(based_fields=['country', 'city', 'street'], zoom=7, null=True)
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


class ProductAmount(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    unit = models.CharField(max_length=10, choices=UNITS, default='kg', help_text='Choose unit')
    related_model = models.ForeignKey('Dish', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class KitchenUtensil(models.Model):

    name = models.CharField(max_length=100, help_text='Enter kitchen utensil name')
    who_added = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_added_to_kitchen_utensil_type', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kitchen_utensil_detail', args=[str(self.id)])


class Dish(models.Model):

    name = models.CharField(max_length=200)
    recipe = models.TextField()
    kitchen_utensils = models.ManyToManyField('KitchenUtensil', blank=False)
    products = models.ManyToManyField('ProductAmount', blank=True)
    who_added = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_added_to_dish_type', null=True)
    favorite = models.ManyToManyField(User, blank=True, related_name='favorite_dish_type')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('dish-detail', args=[str(self.id)])
