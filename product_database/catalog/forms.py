from django import forms
from .models import Store, Product, KitchenUtensil, Profile, HumanAttributes
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from .choices import SEXES, PAGS, UNITS, BIRTH_YEAR_CHOICES, ALL_YEARS
from datetime import date


class DataForCalculatingTheFormulaForm(forms.Form):
    amount_of_days = forms.IntegerField()
    amount_of_money = forms.IntegerField()

    def clean_amount_of_days(self):
        cd = self.cleaned_data
        if cd['amount_of_days'] < 0:
            raise forms.ValidationError("Amount of days can't be lower then one day")
        else:
            self.amount_of_days = cd['amount_of_days']

    def clean_amount_of_money(self):
        cd = self.cleaned_data
        if cd['amount_of_money'] < 1:
            raise forms.ValidationError("Amount of days can't be lower then one")
        else:
            self.amount_of_days = cd['amount_of_money']

class HumanAttributesForm(forms.Form):
    age = forms.ChoiceField(choices= ALL_YEARS)
    sex = forms.ChoiceField(choices=SEXES)
    pag = forms.ChoiceField(choices=PAGS)
    cpa = forms.FloatField()
    weight = forms.FloatField()
    proteins_in_100_g = forms.FloatField()
    proteins_in_100_g_including_animals = forms.FloatField()
    fat_in_100_g = forms.FloatField()
    fat_in_100_g_including_animals = forms.FloatField()
    digestible_carbohydrates_in_100_g = forms.FloatField()
    digestible_carbohydrates_in_100_g_incl_m_and_d = forms.FloatField()
    dietary_fiber_in_100_g = forms.FloatField()
    dietary_fiber_in_100_g_including_fiber_and_pectin = forms.FloatField()
    polyunsaturated_acid = forms.FloatField()
    saturated_acid = forms.FloatField()
    monounsaturated_acid = forms.FloatField()
    calcium_in_100_g_in_mg = forms.FloatField()
    phosphorus_in_100_g_in_mg = forms.FloatField()
    magnesium_in_100_g_in_mg = forms.FloatField()
    potassium_in_100_g_in_mg = forms.FloatField()
    sodium_in_100_g_in_mg = forms.FloatField()
    chlorine_in_100_g_in_mg = forms.FloatField()
    sulfur_in_100_g_in_mg = forms.FloatField()
    iron_in_100_g_in_mg = forms.FloatField()
    zinc_in_100_g_in_mg = forms.FloatField()
    iodine_in_100_g_in_mg = forms.FloatField()
    fluorine_in_100_g_in_mg = forms.FloatField()
    thiamine_vitamin_B1_in_100_g_in_mg = forms.FloatField()
    riboflavin_vitamin_B2_in_100_g_in_mg = forms.FloatField()
    pyridoxine_vitamin_B6_in_100_g_in_mg = forms.FloatField()
    pantothenic_acid_vitamin_B3_in_100_g_in_mg = forms.FloatField()
    folacin_acid_vitamin_B9_in_100_g_in_mcg = forms.FloatField()
    cobalamin_acid_vitamin_B12_in_100_g_in_mcg = forms.FloatField()
    niacin_vitamin_PP_in_100_g_in_mg = forms.FloatField()
    ascorbic_acid_vitamin_C_in_100_g_in_mg = forms.FloatField()
    retinol_vitamin_A_in_100_g_in_mcg = forms.FloatField()
    tocopherol_vitamin_E_in_100_g_in_mg = forms.FloatField()
    cholecalciferol_vitamin_D_in_100_g_in_mcg = forms.FloatField()
    energy_value_in_kcal = forms.FloatField()


# if you need to change country name in BalancedNutritionFormula
#class RenewBalancedNutritionFormula(forms.Form):
#    country = forms.CharField(max_length=255)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    class Meta:
        model = Profile
        fields = ('sex', 'weight', 'nursing', 'cpa', 'city', 'country', 'location')

    def clean_date_of_birth(self):
        cd = self.cleaned_data
        if cd['date_of_birth'] > date.today():
            raise forms.ValidationError('Date of birth is greater then today')


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


class DishForm(forms.Form):
    name = forms.CharField(max_length=200)
    recipe = forms.CharField(max_length=10000)
    kitchen_utensils = forms.ModelMultipleChoiceField(queryset=KitchenUtensil.objects.all())

