from django.contrib import admin
from .models import Product, Store, Price, ProductAmount, KitchenUtensil, Dish
# Register your models here.

# admin.site.register(Product)
# admin.site.register(Store)
# admin.site.register(Price)
# admin.site.register(ProductAmount)
# admin.site.register(KitchenUtensil)
# admin.site.register(Dish)


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
    list_display = ('name', 'location')


@admin.register(ProductAmount)
class ProductAmountAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'unit')


@admin.register(KitchenUtensil)
class KitchenUtensilAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name',)