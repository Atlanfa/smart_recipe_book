from .models import NutritionData


def create_empty_nutrition_data():
    nutrition_data = NutritionData()
    nutrition_data.proteins = 0
    nutrition_data.proteins_including_animals = 0
    nutrition_data.fat = 0
    nutrition_data.fat_including_animals = 0
    nutrition_data.digestible_carbohydrates = 0
    nutrition_data.digestible_carbohydrates_incl_m_and_d = 0
    nutrition_data.dietary_fiber = 0
    nutrition_data.dietary_fiber_including_fiber_and_pectin = 0
    nutrition_data.polyunsaturated_acid = 0
    nutrition_data.saturated_acid = 0
    nutrition_data.monounsaturated_acid = 0
    nutrition_data.calcium_in_mg = 0
    nutrition_data.phosphorus_in_mg = 0
    nutrition_data.magnesium_in_mg = 0
    nutrition_data.potassium_in_mg = 0
    nutrition_data.sodium_in_mg = 0
    nutrition_data.chlorine_in_mg = 0
    nutrition_data.sulfur_in_mg = 0
    nutrition_data.iron_in_mg = 0
    nutrition_data.zinc_in_mg = 0
    nutrition_data.iodine_in_mg = 0
    nutrition_data.fluorine_in_mg = 0
    nutrition_data.thiamine_vitamin_B1_in_mg = 0
    nutrition_data.riboflavin_vitamin_B2_in_mg = 0
    nutrition_data.pyridoxine_vitamin_B6_in_mg = 0
    nutrition_data.pantothenic_acid_vitamin_B3_in_mg = 0
    nutrition_data.folacin_acid_vitamin_B9_in_mcg = 0
    nutrition_data.cobalamin_acid_vitamin_B12_in_mcg = 0
    nutrition_data.niacin_vitamin_PP_in_mg = 0
    nutrition_data.ascorbic_acid_vitamin_C_in_mg = 0
    nutrition_data.retinol_vitamin_A_in_mcg = 0
    nutrition_data.tocopherol_vitamin_E_in_mg = 0
    nutrition_data.cholecalciferol_vitamin_D_in_mcg = 0
    nutrition_data.energy_value_in_kcal = 0
    return nutrition_data


def calculate_dish_nutrition(dish):
    products_amount_list = dish.products
    nutrition_data = create_empty_nutrition_data()
    for product_amount in products_amount_list:
        nutrition_data.proteins += product_amount.product.proteins_in_100_g * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.proteins_including_animals += product_amount.product.proteins_in_100_g_including_animals * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.fat += product_amount.product.fat_in_100_g * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.fat_including_animals += product_amount.product.fat_in_100_g_including_animals * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.digestible_carbohydrates += product_amount.product.digestible_carbohydrates_in_100_g * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.digestible_carbohydrates_incl_m_and_d += product_amount.product.digestible_carbohydrates_in_100_g_incl_m_and_d * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.dietary_fiber += product_amount.product.dietary_fiber_in_100_g * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.dietary_fiber_including_fiber_and_pectin += product_amount.product.dietary_fiber_in_100_g_including_fiber_and_pectin * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.polyunsaturated_acid += product_amount.product.polyunsaturated_acid * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.saturated_acid += product_amount.product.saturated_acid * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.monounsaturated_acid += product_amount.product.monounsaturated_acid * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.calcium_in_mg += product_amount.product.calcium_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.phosphorus_in_mg += product_amount.product.phosphorus_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.magnesium_in_mg += product_amount.product.magnesium_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.potassium_in_mg += product_amount.product.potassium_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.sodium_in_mg += product_amount.product.sodium_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.chlorine_in_mg += product_amount.product.chlorine_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.sulfur_in_mg += product_amount.product.sulfur_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.iron_in_mg += product_amount.product.iron_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.zinc_in_mg += product_amount.product.zinc_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.iodine_in_mg += product_amount.product.iodine_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.fluorine_in_mg += product_amount.product.fluorine_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.thiamine_vitamin_B1_in_mg += product_amount.product.thiamine_vitamin_B1_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.riboflavin_vitamin_B2_in_mg += product_amount.product.riboflavin_vitamin_B2_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.pyridoxine_vitamin_B6_in_mg += product_amount.product.pyridoxine_vitamin_B6_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.pantothenic_acid_vitamin_B3_in_mg += product_amount.product.pantothenic_acid_vitamin_B3_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.folacin_acid_vitamin_B9_in_mcg += product_amount.product.folacin_acid_vitamin_B9_in_100_g_in_mcg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.cobalamin_acid_vitamin_B12_in_mcg += product_amount.product.cobalamin_acid_vitamin_B12_in_100_g_in_mcg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.niacin_vitamin_PP_in_mg += product_amount.product.niacin_vitamin_PP_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.ascorbic_acid_vitamin_C_in_mg += product_amount.product.ascorbic_acid_vitamin_C_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.retinol_vitamin_A_in_mcg += product_amount.product.retinol_vitamin_A_in_100_g_in_mcg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.tocopherol_vitamin_E_in_mg += product_amount.product.tocopherol_vitamin_E_in_100_g_in_mg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.cholecalciferol_vitamin_D_in_mcg += product_amount.product.cholecalciferol_vitamin_D_in_100_g_in_mcg * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
        nutrition_data.energy_value_in_kcal += product_amount.product.energy_value_in_kcal * ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/100)
    return nutrition_data


def calculate_nutrition_for_menu_for_one_day(menu_for_one_day):
    nutrition_data = create_empty_nutrition_data()
    nutrition_data.proteins = calculate_dish_nutrition(menu_for_one_day.breakfast).proteins + calculate_dish_nutrition(menu_for_one_day.diner).proteins + calculate_dish_nutrition(menu_for_one_day.evening_meal).proteins
    nutrition_data.proteins_including_animals = calculate_dish_nutrition(menu_for_one_day.breakfast).proteins_including_animals + calculate_dish_nutrition(menu_for_one_day.diner).proteins_including_animals + calculate_dish_nutrition(menu_for_one_day.evening_meal).proteins_including_animals
    nutrition_data.fat = calculate_dish_nutrition(menu_for_one_day.breakfast).fat + calculate_dish_nutrition(menu_for_one_day.diner).fat + calculate_dish_nutrition(menu_for_one_day.evening_meal).fat
    nutrition_data.fat_including_animals = calculate_dish_nutrition(menu_for_one_day.breakfast).fat_including_animals + calculate_dish_nutrition(menu_for_one_day.diner).fat_including_animals + calculate_dish_nutrition(menu_for_one_day.evening_meal).fat_including_animals
    nutrition_data.digestible_carbohydrates = calculate_dish_nutrition(menu_for_one_day.breakfast).digestible_carbohydrates + calculate_dish_nutrition(menu_for_one_day.diner).digestible_carbohydrates + calculate_dish_nutrition(menu_for_one_day.evening_meal).digestible_carbohydrates
    nutrition_data.digestible_carbohydrates_incl_m_and_d = calculate_dish_nutrition(menu_for_one_day.breakfast).digestible_carbohydrates_incl_m_and_d + calculate_dish_nutrition(menu_for_one_day.diner).digestible_carbohydrates_incl_m_and_d + calculate_dish_nutrition(menu_for_one_day.evening_meal).digestible_carbohydrates_incl_m_and_d
    nutrition_data.dietary_fiber = calculate_dish_nutrition(menu_for_one_day.breakfast).dietary_fiber + calculate_dish_nutrition(menu_for_one_day.diner).dietary_fiber + calculate_dish_nutrition(menu_for_one_day.evening_meal).dietary_fiber
    nutrition_data.dietary_fiber_including_fiber_and_pectin = calculate_dish_nutrition(menu_for_one_day.breakfast).dietary_fiber_including_fiber_and_pectin + calculate_dish_nutrition(menu_for_one_day.diner).dietary_fiber_including_fiber_and_pectin + calculate_dish_nutrition(menu_for_one_day.evening_meal).dietary_fiber_including_fiber_and_pectin
    nutrition_data.polyunsaturated_acid = calculate_dish_nutrition(menu_for_one_day.breakfast).polyunsaturated_acid + calculate_dish_nutrition(menu_for_one_day.diner).polyunsaturated_acid + calculate_dish_nutrition(menu_for_one_day.evening_meal).polyunsaturated_acid
    nutrition_data.saturated_acid = calculate_dish_nutrition(menu_for_one_day.breakfast).saturated_acid + calculate_dish_nutrition(menu_for_one_day.diner).saturated_acid + calculate_dish_nutrition(menu_for_one_day.evening_meal).saturated_acid
    nutrition_data.monounsaturated_acid = calculate_dish_nutrition(menu_for_one_day.breakfast).monounsaturated_acid + calculate_dish_nutrition(menu_for_one_day.diner).monounsaturated_acid + calculate_dish_nutrition(menu_for_one_day.evening_meal).monounsaturated_acid
    nutrition_data.calcium_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).calcium_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).calcium_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).calcium_in_mg
    nutrition_data.phosphorus_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).phosphorus_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).phosphorus_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).phosphorus_in_mg
    nutrition_data.magnesium_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).magnesium_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).magnesium_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).magnesium_in_mg
    nutrition_data.potassium_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).potassium_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).potassium_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).potassium_in_mg
    nutrition_data.sodium_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).sodium_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).sodium_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).sodium_in_mg
    nutrition_data.chlorine_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).chlorine_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).chlorine_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).chlorine_in_mg
    nutrition_data.sulfur_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).sulfur_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).sulfur_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).sulfur_in_mg
    nutrition_data.iron_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).iron_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).iron_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).iron_in_mg
    nutrition_data.zinc_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).zinc_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).zinc_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).zinc_in_mg
    nutrition_data.iodine_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).iodine_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).iodine_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).iodine_in_mg
    nutrition_data.fluorine_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).fluorine_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).fluorine_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).fluorine_in_mg
    nutrition_data.thiamine_vitamin_B1_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).thiamine_vitamin_B1_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).thiamine_vitamin_B1_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).thiamine_vitamin_B1_in_mg
    nutrition_data.riboflavin_vitamin_B2_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).riboflavin_vitamin_B2_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).riboflavin_vitamin_B2_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).riboflavin_vitamin_B2_in_mg
    nutrition_data.pyridoxine_vitamin_B6_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).pyridoxine_vitamin_B6_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).pyridoxine_vitamin_B6_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).pyridoxine_vitamin_B6_in_mg
    nutrition_data.pantothenic_acid_vitamin_B3_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).pantothenic_acid_vitamin_B3_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).pantothenic_acid_vitamin_B3_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).pantothenic_acid_vitamin_B3_in_mg
    nutrition_data.folacin_acid_vitamin_B9_in_mcg = calculate_dish_nutrition(menu_for_one_day.breakfast).folacin_acid_vitamin_B9_in_mcg + calculate_dish_nutrition(menu_for_one_day.diner).folacin_acid_vitamin_B9_in_mcg + calculate_dish_nutrition(menu_for_one_day.evening_meal).folacin_acid_vitamin_B9_in_mcg
    nutrition_data.cobalamin_acid_vitamin_B12_in_mcg = calculate_dish_nutrition(menu_for_one_day.breakfast).cobalamin_acid_vitamin_B12_in_mcg + calculate_dish_nutrition(menu_for_one_day.diner).cobalamin_acid_vitamin_B12_in_mcg + calculate_dish_nutrition(menu_for_one_day.evening_meal).cobalamin_acid_vitamin_B12_in_mcg
    nutrition_data.niacin_vitamin_PP_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).niacin_vitamin_PP_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).niacin_vitamin_PP_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).niacin_vitamin_PP_in_mg
    nutrition_data.ascorbic_acid_vitamin_C_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).ascorbic_acid_vitamin_C_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).ascorbic_acid_vitamin_C_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).ascorbic_acid_vitamin_C_in_mg
    nutrition_data.retinol_vitamin_A_in_mcg = calculate_dish_nutrition(menu_for_one_day.breakfast).retinol_vitamin_A_in_mcg + calculate_dish_nutrition(menu_for_one_day.diner).retinol_vitamin_A_in_mcg + calculate_dish_nutrition(menu_for_one_day.evening_meal).retinol_vitamin_A_in_mcg
    nutrition_data.tocopherol_vitamin_E_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).tocopherol_vitamin_E_in_mg + calculate_dish_nutrition(menu_for_one_day.diner).tocopherol_vitamin_E_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).tocopherol_vitamin_E_in_mg
    nutrition_data.cholecalciferol_vitamin_D_in_mcg = calculate_dish_nutrition(menu_for_one_day.breakfast).cholecalciferol_vitamin_D_in_mcg + calculate_dish_nutrition(menu_for_one_day.diner).cholecalciferol_vitamin_D_in_mcg + calculate_dish_nutrition(menu_for_one_day.evening_meal).cholecalciferol_vitamin_D_in_mcg
    nutrition_data.energy_value_in_kcal = calculate_dish_nutrition(menu_for_one_day.breakfast).energy_value_in_kcal + calculate_dish_nutrition(menu_for_one_day.diner).energy_value_in_kcal + calculate_dish_nutrition(menu_for_one_day.evening_meal).energy_value_in_kcal
    return nutrition_data