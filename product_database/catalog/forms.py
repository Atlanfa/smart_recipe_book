from django import forms
from .models import Store, Product, UNITS, KitchenUtensil, ProductAmount
from django.contrib.auth.models import User


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=200, help_text="Enter product name")
    who_added = forms.ModelChoiceField(queryset=User.objects.all())


class AddStoreForm(forms.Form):
    name = forms.CharField(max_length=50, help_text="Enter a store name")
    location = forms.CharField(max_length=100, help_text="Enter store location")
    who_added = forms.ModelChoiceField(queryset=User.objects.all())


class AddPriceForm(forms.Form):
    store = forms.ModelChoiceField(queryset=Store.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    who_added = forms.ModelChoiceField(queryset=User.objects.all())


class RenewProductForm(forms.Form):
    name = forms.CharField(max_length=200, help_text="Enter product name")


class RenewStoreForm(forms.Form):
    name = forms.CharField(max_length=50, help_text="Enter a store name")
    location = forms.CharField(max_length=100, help_text="Enter store location")


class RenewPriceForm(forms.Form):
    price = forms.DecimalField(max_digits=10, decimal_places=2)


class ProductAmountForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    amount = forms.DecimalField(max_digits=10, decimal_places=3)
    unit = forms.ChoiceField(choices=UNITS)


class AddKitchenUtensilForm(forms.Form):
    name = forms.CharField(max_length=100, help_text='Enter kitchen utensil name')
    who_added = forms.ModelChoiceField(queryset=User.objects.all())


class RenewKitchenUtensilForm(forms.Form):
    name = forms.CharField(max_length=100, help_text='Enter kitchen utensil name')


class AddDishForm(forms.Form):
    name = forms.CharField(max_length=200)
    recipe = forms.CharField(max_length=10000)
    kitchen_utensils = forms.ModelMultipleChoiceField(queryset=KitchenUtensil.objects.all())

class RenewDishForm(forms.Form):
    name = forms.CharField(max_length=200)
    recipe = forms.CharField(max_length=10000)
    kitchen_utensils = forms.ModelChoiceField(queryset=KitchenUtensil.objects.all())
    products = forms.ModelChoiceField(queryset=ProductAmount.objects.all())
