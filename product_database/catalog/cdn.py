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
    products_amount_list = dish.products.all()
    nutrition_data = create_empty_nutrition_data()
    for product_amount in products_amount_list:
        untits_multiplayer = (product_amount.amount * 1000 if product_amount.unit in ['kg', 'l'] else 100)/100
        print(untits_multiplayer)
        nutrition_data.proteins += float(product_amount.product.proteins_in_100_g) * float(untits_multiplayer)
        nutrition_data.proteins_including_animals += float(product_amount.product.proteins_in_100_g_including_animals) * float( untits_multiplayer)
        nutrition_data.fat += float(product_amount.product.fat_in_100_g) * float( untits_multiplayer)
        nutrition_data.fat_including_animals += float(product_amount.product.fat_in_100_g_including_animals) * float( untits_multiplayer)
        nutrition_data.digestible_carbohydrates += float(product_amount.product.digestible_carbohydrates_in_100_g) * float( untits_multiplayer)
        nutrition_data.digestible_carbohydrates_incl_m_and_d += float(product_amount.product.digestible_carbohydrates_in_100_g_incl_m_and_d ) * float( untits_multiplayer)
        nutrition_data.dietary_fiber += float(product_amount.product.dietary_fiber_in_100_g ) * float( untits_multiplayer)
        nutrition_data.dietary_fiber_including_fiber_and_pectin += float(product_amount.product.dietary_fiber_in_100_g_including_fiber_and_pectin ) * float( untits_multiplayer)
        nutrition_data.polyunsaturated_acid += float(product_amount.product.polyunsaturated_acid ) * float( untits_multiplayer)
        nutrition_data.saturated_acid += float(product_amount.product.saturated_acid ) * float( untits_multiplayer)
        nutrition_data.monounsaturated_acid += float(product_amount.product.monounsaturated_acid ) * float( untits_multiplayer)
        nutrition_data.calcium_in_mg += float(product_amount.product.calcium_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.phosphorus_in_mg += float(product_amount.product.phosphorus_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.magnesium_in_mg += float(product_amount.product.magnesium_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.potassium_in_mg += float(product_amount.product.potassium_in_100_g_in_mg ) * float(untits_multiplayer)
        nutrition_data.sodium_in_mg += float(product_amount.product.sodium_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.chlorine_in_mg += float(product_amount.product.chlorine_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.sulfur_in_mg += float(product_amount.product.sulfur_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.iron_in_mg += float(product_amount.product.iron_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.zinc_in_mg += float(product_amount.product.zinc_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.iodine_in_mg += float(product_amount.product.iodine_in_100_g_in_mg) * float( untits_multiplayer)
        nutrition_data.fluorine_in_mg += float(product_amount.product.fluorine_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.thiamine_vitamin_B1_in_mg += float(product_amount.product.thiamine_vitamin_B1_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.riboflavin_vitamin_B2_in_mg += float(product_amount.product.riboflavin_vitamin_B2_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.pyridoxine_vitamin_B6_in_mg += float(product_amount.product.pyridoxine_vitamin_B6_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.pantothenic_acid_vitamin_B3_in_mg += float(product_amount.product.pantothenic_acid_vitamin_B3_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.folacin_acid_vitamin_B9_in_mcg += float(product_amount.product.folacin_acid_vitamin_B9_in_100_g_in_mcg ) * float( untits_multiplayer)
        nutrition_data.cobalamin_acid_vitamin_B12_in_mcg += float(product_amount.product.cobalamin_acid_vitamin_B12_in_100_g_in_mcg ) * float( untits_multiplayer)
        nutrition_data.niacin_vitamin_PP_in_mg += float(product_amount.product.niacin_vitamin_PP_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.ascorbic_acid_vitamin_C_in_mg += float(product_amount.product.ascorbic_acid_vitamin_C_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.retinol_vitamin_A_in_mcg += float(product_amount.product.retinol_vitamin_A_in_100_g_in_mcg ) * float( untits_multiplayer)
        nutrition_data.tocopherol_vitamin_E_in_mg += float(product_amount.product.tocopherol_vitamin_E_in_100_g_in_mg ) * float( untits_multiplayer)
        nutrition_data.cholecalciferol_vitamin_D_in_mcg += float(product_amount.product.cholecalciferol_vitamin_D_in_100_g_in_mcg) * float(untits_multiplayer)
        nutrition_data.energy_value_in_kcal += float(product_amount.product.energy_value_in_kcal) * float(untits_multiplayer)
    return nutrition_data


def calculate_nutrition_for_menu_for_one_day(menu_for_one_day):
    nutrition_data = create_empty_nutrition_data()
    nutrition_data.proteins = calculate_dish_nutrition(menu_for_one_day.breakfast).proteins + calculate_dish_nutrition(menu_for_one_day.dinner).proteins + calculate_dish_nutrition(menu_for_one_day.evening_meal).proteins
    nutrition_data.proteins_including_animals = calculate_dish_nutrition(menu_for_one_day.breakfast).proteins_including_animals + calculate_dish_nutrition(menu_for_one_day.dinner).proteins_including_animals + calculate_dish_nutrition(menu_for_one_day.evening_meal).proteins_including_animals
    nutrition_data.fat = calculate_dish_nutrition(menu_for_one_day.breakfast).fat + calculate_dish_nutrition(menu_for_one_day.dinner).fat + calculate_dish_nutrition(menu_for_one_day.evening_meal).fat
    nutrition_data.fat_including_animals = calculate_dish_nutrition(menu_for_one_day.breakfast).fat_including_animals + calculate_dish_nutrition(menu_for_one_day.dinner).fat_including_animals + calculate_dish_nutrition(menu_for_one_day.evening_meal).fat_including_animals
    nutrition_data.digestible_carbohydrates = calculate_dish_nutrition(menu_for_one_day.breakfast).digestible_carbohydrates + calculate_dish_nutrition(menu_for_one_day.dinner).digestible_carbohydrates + calculate_dish_nutrition(menu_for_one_day.evening_meal).digestible_carbohydrates
    nutrition_data.digestible_carbohydrates_incl_m_and_d = calculate_dish_nutrition(menu_for_one_day.breakfast).digestible_carbohydrates_incl_m_and_d + calculate_dish_nutrition(menu_for_one_day.dinner).digestible_carbohydrates_incl_m_and_d + calculate_dish_nutrition(menu_for_one_day.evening_meal).digestible_carbohydrates_incl_m_and_d
    nutrition_data.dietary_fiber = calculate_dish_nutrition(menu_for_one_day.breakfast).dietary_fiber + calculate_dish_nutrition(menu_for_one_day.dinner).dietary_fiber + calculate_dish_nutrition(menu_for_one_day.evening_meal).dietary_fiber
    nutrition_data.dietary_fiber_including_fiber_and_pectin = calculate_dish_nutrition(menu_for_one_day.breakfast).dietary_fiber_including_fiber_and_pectin + calculate_dish_nutrition(menu_for_one_day.dinner).dietary_fiber_including_fiber_and_pectin + calculate_dish_nutrition(menu_for_one_day.evening_meal).dietary_fiber_including_fiber_and_pectin
    nutrition_data.polyunsaturated_acid = calculate_dish_nutrition(menu_for_one_day.breakfast).polyunsaturated_acid + calculate_dish_nutrition(menu_for_one_day.dinner).polyunsaturated_acid + calculate_dish_nutrition(menu_for_one_day.evening_meal).polyunsaturated_acid
    nutrition_data.saturated_acid = calculate_dish_nutrition(menu_for_one_day.breakfast).saturated_acid + calculate_dish_nutrition(menu_for_one_day.dinner).saturated_acid + calculate_dish_nutrition(menu_for_one_day.evening_meal).saturated_acid
    nutrition_data.monounsaturated_acid = calculate_dish_nutrition(menu_for_one_day.breakfast).monounsaturated_acid + calculate_dish_nutrition(menu_for_one_day.dinner).monounsaturated_acid + calculate_dish_nutrition(menu_for_one_day.evening_meal).monounsaturated_acid
    nutrition_data.calcium_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).calcium_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).calcium_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).calcium_in_mg
    nutrition_data.phosphorus_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).phosphorus_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).phosphorus_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).phosphorus_in_mg
    nutrition_data.magnesium_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).magnesium_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).magnesium_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).magnesium_in_mg
    nutrition_data.potassium_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).potassium_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).potassium_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).potassium_in_mg
    nutrition_data.sodium_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).sodium_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).sodium_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).sodium_in_mg
    nutrition_data.chlorine_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).chlorine_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).chlorine_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).chlorine_in_mg
    nutrition_data.sulfur_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).sulfur_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).sulfur_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).sulfur_in_mg
    nutrition_data.iron_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).iron_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).iron_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).iron_in_mg
    nutrition_data.zinc_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).zinc_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).zinc_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).zinc_in_mg
    nutrition_data.iodine_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).iodine_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).iodine_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).iodine_in_mg
    nutrition_data.fluorine_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).fluorine_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).fluorine_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).fluorine_in_mg
    nutrition_data.thiamine_vitamin_B1_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).thiamine_vitamin_B1_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).thiamine_vitamin_B1_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).thiamine_vitamin_B1_in_mg
    nutrition_data.riboflavin_vitamin_B2_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).riboflavin_vitamin_B2_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).riboflavin_vitamin_B2_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).riboflavin_vitamin_B2_in_mg
    nutrition_data.pyridoxine_vitamin_B6_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).pyridoxine_vitamin_B6_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).pyridoxine_vitamin_B6_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).pyridoxine_vitamin_B6_in_mg
    nutrition_data.pantothenic_acid_vitamin_B3_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).pantothenic_acid_vitamin_B3_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).pantothenic_acid_vitamin_B3_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).pantothenic_acid_vitamin_B3_in_mg
    nutrition_data.folacin_acid_vitamin_B9_in_mcg = calculate_dish_nutrition(menu_for_one_day.breakfast).folacin_acid_vitamin_B9_in_mcg + calculate_dish_nutrition(menu_for_one_day.dinner).folacin_acid_vitamin_B9_in_mcg + calculate_dish_nutrition(menu_for_one_day.evening_meal).folacin_acid_vitamin_B9_in_mcg
    nutrition_data.cobalamin_acid_vitamin_B12_in_mcg = calculate_dish_nutrition(menu_for_one_day.breakfast).cobalamin_acid_vitamin_B12_in_mcg + calculate_dish_nutrition(menu_for_one_day.dinner).cobalamin_acid_vitamin_B12_in_mcg + calculate_dish_nutrition(menu_for_one_day.evening_meal).cobalamin_acid_vitamin_B12_in_mcg
    nutrition_data.niacin_vitamin_PP_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).niacin_vitamin_PP_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).niacin_vitamin_PP_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).niacin_vitamin_PP_in_mg
    nutrition_data.ascorbic_acid_vitamin_C_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).ascorbic_acid_vitamin_C_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).ascorbic_acid_vitamin_C_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).ascorbic_acid_vitamin_C_in_mg
    nutrition_data.retinol_vitamin_A_in_mcg = calculate_dish_nutrition(menu_for_one_day.breakfast).retinol_vitamin_A_in_mcg + calculate_dish_nutrition(menu_for_one_day.dinner).retinol_vitamin_A_in_mcg + calculate_dish_nutrition(menu_for_one_day.evening_meal).retinol_vitamin_A_in_mcg
    nutrition_data.tocopherol_vitamin_E_in_mg = calculate_dish_nutrition(menu_for_one_day.breakfast).tocopherol_vitamin_E_in_mg + calculate_dish_nutrition(menu_for_one_day.dinner).tocopherol_vitamin_E_in_mg + calculate_dish_nutrition(menu_for_one_day.evening_meal).tocopherol_vitamin_E_in_mg
    nutrition_data.cholecalciferol_vitamin_D_in_mcg = calculate_dish_nutrition(menu_for_one_day.breakfast).cholecalciferol_vitamin_D_in_mcg + calculate_dish_nutrition(menu_for_one_day.dinner).cholecalciferol_vitamin_D_in_mcg + calculate_dish_nutrition(menu_for_one_day.evening_meal).cholecalciferol_vitamin_D_in_mcg
    nutrition_data.energy_value_in_kcal = calculate_dish_nutrition(menu_for_one_day.breakfast).energy_value_in_kcal + calculate_dish_nutrition(menu_for_one_day.dinner).energy_value_in_kcal + calculate_dish_nutrition(menu_for_one_day.evening_meal).energy_value_in_kcal
    return nutrition_data