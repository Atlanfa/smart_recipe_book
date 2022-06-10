from random import choice

from catalog.citmmtf import check_if_the_menu_matches_the_formula
from catalog.cp import calculate_price
from .models import MenuForOneDay


def balanced_nutrition_formula_menu_calculation(dishes_list, amount_of_days, amount_of_money, user_data, bnf):
    global menu
    menu_is_ready = False
    while not menu_is_ready:
        menu = []
        money_left = amount_of_money
        no_money = False
        i = 1
        for day in range(amount_of_days):
            print(f'calculating day {i}')
            day_ready = False
            while not day_ready:
                i += 1
                breakfast = choice(dishes_list)
                dinner = choice(dishes_list)
                evening_meal = choice(dishes_list)
                menu_for_one_day = MenuForOneDay()
                menu_for_one_day.breakfast = breakfast
                menu_for_one_day.dinner = dinner
                menu_for_one_day.evening_meal = evening_meal
                money_left_temp = money_left - (calculate_price(menu_for_one_day.breakfast, user_data) + calculate_price(menu_for_one_day.dinner, user_data) + calculate_price(menu_for_one_day.evening_meal, user_data))
                if money_left_temp > 0:
                    if check_if_the_menu_matches_the_formula(menu_for_one_day, bnf, user_data):
                        menu.append(menu_for_one_day)
                        print(menu_for_one_day.evening_meal.name)
                        money_left = money_left - (calculate_price(menu_for_one_day.breakfast, user_data) + calculate_price(menu_for_one_day.dinner, user_data) + calculate_price(menu_for_one_day.evening_meal, user_data))
                        day_ready = True
            #     else:
            #         no_money = True
            #         break
            # if no_money:
            #     break
        menu_is_ready = True
    for i in menu:
        i.save()
    print(menu)
    print(menu[0].evening_meal.name)
    return menu
