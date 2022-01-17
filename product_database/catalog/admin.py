from django.contrib import admin
from .models import Product, Store, Price, ProductAmount, KitchenUtensil, Dish, Profile, HumanAttributes, BalancedNutritionFormula
# Register your models here.

# admin.site.register(Product)
# admin.site.register(Store)
# admin.site.register(Price)
# admin.site.register(ProductAmount)
# admin.site.register(KitchenUtensil)
# admin.site.register(Dish)
#from .regions import get_regions
#from .data_dict import data
#from .models import BalancedNutritionFormula

#for country in get_regions(data):
#    BalancedNutritionFormula.objects.create(country=country)


@admin.register(HumanAttributes)
class HumanAttributesAdmin(admin.ModelAdmin):
    list_display = ('age', 'sex', 'weight', 'related_model')


class HumanAttributesInline(admin.TabularInline):
    model = HumanAttributes


@admin.register(BalancedNutritionFormula)
class BalancedNutritionFormulaAdmin(admin.ModelAdmin):
    list_display = ('country',)
    inlines = [HumanAttributesInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth', 'sex', 'weight', 'nursing', 'cpa', 'country', 'city', 'location')


class PriceInline(admin.TabularInline):
    model = Price


class FavoriteInline(admin.TabularInline):
    model = Product.favorite.through


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'price')
    list_filter = ('product', 'store')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [PriceInline, FavoriteInline]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'street', 'location')


@admin.register(ProductAmount)
class ProductAmountAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'unit')


@admin.register(KitchenUtensil)
class KitchenUtensilAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name',)
