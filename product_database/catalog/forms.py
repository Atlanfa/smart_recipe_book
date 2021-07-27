from django import forms
from .models import Store, Product, KitchenUtensil
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from .choices import SEXES, CPAS, UNITS, BIRTH_YEAR_CHOICES


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')


class ProfileEditForm(forms.Form):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    sex = forms.ChoiceField(choices=SEXES)
    weight = forms.FloatField()
    nursing = forms.BooleanField()
    kid_date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    cpa = forms.ChoiceField(choices=CPAS)
    city = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    location = PlainLocationField(based_fields=['country', 'city'], zoom=7)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


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
    street = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    location = PlainLocationField(based_fields=['country', 'city', 'street'], zoom=7)


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
