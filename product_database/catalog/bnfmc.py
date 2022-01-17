from .models import MenuForOneDay
from random import choice
from .cdn import calculate_nutrition_for_menu_for_one_day
from .cp import calculate_price
from .citmmtf import check_if_the_menu_matches_the_formula


def balanced_nutrition_formula_menu_calculation(dishes_list, amount_of_days, amount_of_money, user_data, bnf):
    menu_is_ready = False
    menu = []
    while not menu_is_ready:
        money_left = amount_of_money
        for day in range(amount_of_days):
            day_ready = False
            while not day_ready:
                breakfast = choice(dishes_list)
                dinner = choice(dishes_list)
                evening_meal = choice(dishes_list)
                menu_for_one_day = MenuForOneDay()
                menu_for_one_day.breakfast = breakfast
                menu_for_one_day.dinner = dinner
                menu_for_one_day.evening_meal = evening_meal
                money_left_temp = money_left - (calculate_price(menu_for_one_day.breakfast, user_data) + calculate_price(menu_for_one_day.dinner, user_data) + calculate_price(menu_for_one_day, user_data))
                if money_left_temp > 0:
                    if check_if_the_menu_matches_the_formula(menu_for_one_day, bnf, user_data):
                        menu.append(menu_for_one_day)
                        money_left = money_left - (calculate_price(menu_for_one_day.breakfast, user_data) + calculate_price(menu_for_one_day.dinner, user_data) + calculate_price(menu_for_one_day, user_data))
                        day_ready = calculate_nutrition_for_menu_for_one_day(menu_for_one_day)
            menu_is_ready = True
    return menu
