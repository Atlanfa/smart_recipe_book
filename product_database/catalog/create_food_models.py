from catalog.models import Product, Price, ProductAmount, Store, Dish, KitchenUtensil
from django.contrib.auth.models import User


def create_food():
    user = User.objects.create_user(username='testuser', password='12345')
    user.save()
    store1 = Store.objects.create(name='Store1', country='Ukraine', city='Kherson', street='Ushakova 50', location=None,
                                  who_added=user)
    store2 = Store.objects.create(name='Store2', country='Ukraine', city='Kherson', street='Ushakova 49', location=None,
                                  who_added=user)
    store1.save()
    store2.save()

    product_list = []
    for i in range(1, 7):
        product = Product.objects.create(name=f'Product{i}', who_added=user, weight=100, unit='g', product_by_weight_in_packaging='n',proteins_in_100_g = 14.66
        ,proteins_in_100_g_including_animals = 8
        ,fat_in_100_g = 17.83
        ,fat_in_100_g_including_animals = 5.33
        ,digestible_carbohydrates_in_100_g = 70.33
        ,digestible_carbohydrates_in_100_g_incl_m_and_d = 12.5
        ,dietary_fiber_in_100_g = 3.75
        ,dietary_fiber_in_100_g_including_fiber_and_pectin = 2.08
        ,polyunsaturated_acid = 0
        ,saturated_acid = 0
        ,monounsaturated_acid = 0
        ,calcium_in_100_g_in_mg = 133.33
        ,phosphorus_in_100_g_in_mg = 200
        ,magnesium_in_100_g_in_mg = 66.66
        ,potassium_in_100_g_in_mg = 625
        ,sodium_in_100_g_in_mg = 833.33
        ,chlorine_in_100_g_in_mg = 1416.66
        ,sulfur_in_100_g_in_mg = 166.66
        ,iron_in_100_g_in_mg = 2.33
        ,zinc_in_100_g_in_mg = 2.5
        ,iodine_in_100_g_in_mg = 0.025
        ,fluorine_in_100_g_in_mg = 0.5
        ,thiamine_vitamin_B1_in_100_g_in_mg = 0.26
        ,riboflavin_vitamin_B2_in_100_g_in_mg = 0.3
        ,pyridoxine_vitamin_B6_in_100_g_in_mg = 0.316
        ,pantothenic_acid_vitamin_B3_in_100_g_in_mg = 2.083
        ,folacin_acid_vitamin_B9_in_100_g_in_mcg = 33.33
        ,cobalamin_acid_vitamin_B12_in_100_g_in_mcg = 0.5
        ,niacin_vitamin_PP_in_100_g_in_mg = 3.5
        ,ascorbic_acid_vitamin_C_in_100_g_in_mg =14.16
        ,retinol_vitamin_A_in_100_g_in_mcg = 150
        ,tocopherol_vitamin_E_in_100_g_in_mg = 1.5
        ,cholecalciferol_vitamin_D_in_100_g_in_mcg = 0.416
        ,energy_value_in_kcal = 500)

        product.save()
        product_list.append(product)

    price_list = []
    for i in range(1,4):
        price = Price.objects.create(store=store1, product=product_list[i-1], price=16.66, who_added=user)
        price.save()
        price_list.append(price)
    for i in range(4,7):
        price = Price.objects.create(store=store2, product=product_list[i-1], price=16.66, who_added=user)
        price.save()
        price_list.append(price)

    kitchen_utensil = KitchenUtensil.objects.create(name='Kitchen utensil 1', who_added=user)
    kitchen_utensil.save()

    dish_list = []
    for i in range(3):
        dish = Dish.objects.create(name=f'Dish{i+1}', recipe=f'Recipe for dish{i+1}', who_added=user)
        dish.kitchen_utensils.add(kitchen_utensil)
        dish.save()
        product_amount1 = ProductAmount(product=product_list[0], amount=100.0, unit='g', related_model=dish)
        product_amount2 = ProductAmount(product=product_list[1], amount=100.0, unit='g', related_model=dish)
        product_list.pop(0)
        product_list.pop(0)
        product_amount1.save()
        product_amount2.save()
        product_amount_list = [product_amount1, product_amount2]
        dish.products.set(product_amount_list)
        dish.save()
        dish_list.append(dish)