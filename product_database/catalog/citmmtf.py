from .cdn import calculate_nutrition_for_menu_for_one_day
from datetime import datetime


def check_if_the_menu_matches_the_formula(menu_for_one_day, bnf, user_data):
    nutrition_data = calculate_nutrition_for_menu_for_one_day(menu_for_one_day)
    age = [datetime.now().year - user_data.date_of_birth.year] if (datetime.now().year - user_data.date_of_birth.year) > 1 else [datetime.datetime.now().month - user_data.date_of_birth.mount, 'm']
    is_correct = False
    for human_attributes in bnf.human_attributes:
        age_choices = human_attributes.age[:-1].split('-').append('m') if 'm' in human_attributes.age else human_attributes.age.split('-')
        if 'm' in age_choices:
            if 'm' in age:
                if age[0] in range(age_choices[0], age_choices[1]):
                    if nutrition_data.proteins in range(human_attributes.proteins-10, human_attributes.proteins + 10) and nutrition_data.proteins_including_animals in range(human_attributes.proteins_including_animals-10, human_attributes.proteins_including_animals + 10) and nutrition_data.fat in range(human_attributes.fat-10, human_attributes.fat + 10) and nutrition_data.fat_including_animals in range(human_attributes.fat_including_animals-10, human_attributes.fat_including_animals + 10) and nutrition_data.digestible_carbohydrates in range(human_attributes.digestible_carbohydrates-30, human_attributes.digestible_carbohydrates + 30) and nutrition_data.digestible_carbohydrates_incl_m_and_d in range(human_attributes.digestible_carbohydrates_incl_m_and_d-30, human_attributes.digestible_carbohydrates_incl_m_and_d + 30) and nutrition_data.dietary_fiber in range(human_attributes.dietary_fiber - 4, human_attributes.dietary_fiber + 4) and nutrition_data.dietary_fiber_including_fiber_and_pectin in range(human_attributes.dietary_fiber_including_fiber_and_pectin-4, human_attributes.dietary_fiber_including_fiber_and_pectin + 4) and nutrition_data.polyunsaturated_acid in range(human_attributes.polyunsaturated_acid-3, human_attributes.polyunsaturated_acid + 3) and nutrition_data.saturated_acid in range(human_attributes.saturated_acid-5, human_attributes.saturated_acid + 5) and nutrition_data.monounsaturated_acid in range(human_attributes.monounsaturated_acid-6, human_attributes.monounsaturated_acid + 6) and nutrition_data.calcium_in_mg in range(human_attributes.calcium_in_mg-90, human_attributes.calcium_in_mg + 90) and nutrition_data.phosphorus_in_mg in range(human_attributes.phosphorus_in_mg-100, human_attributes.phosphorus_in_mg + 100) and nutrition_data.magnesium_in_mg in range(human_attributes.magnesium_in_mg-60, human_attributes.magnesium_in_mg + 60) and nutrition_data.potassium_in_mg in range(human_attributes.potassium_in_mg-1000, human_attributes.potassium_in_mg + 1000) and nutrition_data.sodium_in_mg in range(human_attributes.sodium_in_mg-900, human_attributes.sodium_in_mg + 900) and nutrition_data.chlorine_in_mg in range(human_attributes.chlorine_in_mg-100, human_attributes.chlorine_in_mg + 1000) and nutrition_data.sulfur_in_mg in range(human_attributes.sulfur_in_mg-200, human_attributes.sulfur_in_mg + 200) and nutrition_data.iron_in_mg in range(human_attributes.iron_in_mg-4, human_attributes.iron_in_mg + 4) and nutrition_data.zinc_in_mg in range(human_attributes.zinc_in_mg-3, human_attributes.zinc_in_mg + 3) and nutrition_data.iodine_in_mg in range(human_attributes.iodine_in_mg-0.4, human_attributes.iodine_in_mg + 0.4) and nutrition_data.fluorine_in_mg in range(human_attributes.fluorine_in_mg-2, human_attributes.fluorine_in_mg + 2) and nutrition_data.thiamine_vitamin_B1_in_mg in range(human_attributes.thiamine_vitamin_B1_in_mg-0.6, human_attributes.thiamine_vitamin_B1_in_mg + 0.6) and nutrition_data.riboflavin_vitamin_B2_in_mg in range(human_attributes.riboflavin_vitamin_B2_in_mg-0.7, human_attributes.riboflavin_vitamin_B2_in_mg + 0.7) and nutrition_data.pyridoxine_vitamin_B6_in_mg in range(human_attributes.pyridoxine_vitamin_B6_in_mg-0.4, human_attributes.pyridoxine_vitamin_B6_in_mg + 0.4) and nutrition_data.pantothenic_acid_vitamin_B3_in_mg in range(human_attributes.pantothenic_acid_vitamin_B3_in_mg-2.5, human_attributes.pantothenic_acid_vitamin_B3_in_mg + 2.5) and nutrition_data.folacin_acid_vitamin_B9_in_mcg in range(human_attributes.folacin_acid_vitamin_B9_in_mcg-30, human_attributes.folacin_acid_vitamin_B9_in_mcg + 30) and nutrition_data.cobalamin_acid_vitamin_B12_in_mcg in range(human_attributes.cobalamin_acid_vitamin_B12_in_mcg-2, human_attributes.cobalamin_acid_vitamin_B12_in_mcg + 2) and nutrition_data.niacin_vitamin_PP_in_mg in range(human_attributes.niacin_vitamin_PP_in_mg-6, human_attributes.niacin_vitamin_PP_in_mg + 6) and nutrition_data.ascorbic_acid_vitamin_C_in_mg in range(human_attributes.ascorbic_acid_vitamin_C_in_mg-15, human_attributes.ascorbic_acid_vitamin_C_in_mg + 15) and nutrition_data.retinol_vitamin_A_in_mcg in range(human_attributes.retinol_vitamin_A_in_mcg-100, human_attributes.retinol_vitamin_A_in_mcg + 100) and nutrition_data.tocopherol_vitamin_E_in_mg in range(human_attributes.tocopherol_vitamin_E_in_mg-1, human_attributes.tocopherol_vitamin_E_in_mg + 1) and nutrition_data.cholecalciferol_vitamin_D_in_mcg in range(human_attributes.cholecalciferol_vitamin_D_in_mcg-1.1, human_attributes.cholecalciferol_vitamin_D_in_mcg + 1.1) and nutrition_data.energy_value_in_kcal in range(human_attributes.energy_value_in_kcal-350, human_attributes.energy_value_in_kcal + 350):
                        is_correct = True
        else:
            if age[0] in range(age_choices[0], age_choices[1]):
                if nutrition_data.proteins in range(human_attributes.proteins - 10,
                                                    human_attributes.proteins + 10) and nutrition_data.proteins_including_animals in range(
                        human_attributes.proteins_including_animals - 10,
                        human_attributes.proteins_including_animals + 10) and nutrition_data.fat in range(
                        human_attributes.fat - 10,
                        human_attributes.fat + 10) and nutrition_data.fat_including_animals in range(
                        human_attributes.fat_including_animals - 10,
                        human_attributes.fat_including_animals + 10) and nutrition_data.digestible_carbohydrates in range(
                        human_attributes.digestible_carbohydrates - 30,
                        human_attributes.digestible_carbohydrates + 30) and nutrition_data.digestible_carbohydrates_incl_m_and_d in range(
                        human_attributes.digestible_carbohydrates_incl_m_and_d - 30,
                        human_attributes.digestible_carbohydrates_incl_m_and_d + 30) and nutrition_data.dietary_fiber in range(
                        human_attributes.dietary_fiber - 4,
                        human_attributes.dietary_fiber + 4) and nutrition_data.dietary_fiber_including_fiber_and_pectin in range(
                        human_attributes.dietary_fiber_including_fiber_and_pectin - 4,
                        human_attributes.dietary_fiber_including_fiber_and_pectin + 4) and nutrition_data.polyunsaturated_acid in range(
                        human_attributes.polyunsaturated_acid - 3,
                        human_attributes.polyunsaturated_acid + 3) and nutrition_data.saturated_acid in range(
                        human_attributes.saturated_acid - 5,
                        human_attributes.saturated_acid + 5) and nutrition_data.monounsaturated_acid in range(
                        human_attributes.monounsaturated_acid - 6,
                        human_attributes.monounsaturated_acid + 6) and nutrition_data.calcium_in_mg in range(
                        human_attributes.calcium_in_mg - 90,
                        human_attributes.calcium_in_mg + 90) and nutrition_data.phosphorus_in_mg in range(
                        human_attributes.phosphorus_in_mg - 100,
                        human_attributes.phosphorus_in_mg + 100) and nutrition_data.magnesium_in_mg in range(
                        human_attributes.magnesium_in_mg - 60,
                        human_attributes.magnesium_in_mg + 60) and nutrition_data.potassium_in_mg in range(
                        human_attributes.potassium_in_mg - 1000,
                        human_attributes.potassium_in_mg + 1000) and nutrition_data.sodium_in_mg in range(
                        human_attributes.sodium_in_mg - 900,
                        human_attributes.sodium_in_mg + 900) and nutrition_data.chlorine_in_mg in range(
                        human_attributes.chlorine_in_mg - 100,
                        human_attributes.chlorine_in_mg + 1000) and nutrition_data.sulfur_in_mg in range(
                        human_attributes.sulfur_in_mg - 200,
                        human_attributes.sulfur_in_mg + 200) and nutrition_data.iron_in_mg in range(
                        human_attributes.iron_in_mg - 4,
                        human_attributes.iron_in_mg + 4) and nutrition_data.zinc_in_mg in range(
                        human_attributes.zinc_in_mg - 3,
                        human_attributes.zinc_in_mg + 3) and nutrition_data.iodine_in_mg in range(
                        human_attributes.iodine_in_mg - 0.4,
                        human_attributes.iodine_in_mg + 0.4) and nutrition_data.fluorine_in_mg in range(
                        human_attributes.fluorine_in_mg - 2,
                        human_attributes.fluorine_in_mg + 2) and nutrition_data.thiamine_vitamin_B1_in_mg in range(
                        human_attributes.thiamine_vitamin_B1_in_mg - 0.6,
                        human_attributes.thiamine_vitamin_B1_in_mg + 0.6) and nutrition_data.riboflavin_vitamin_B2_in_mg in range(
                        human_attributes.riboflavin_vitamin_B2_in_mg - 0.7,
                        human_attributes.riboflavin_vitamin_B2_in_mg + 0.7) and nutrition_data.pyridoxine_vitamin_B6_in_mg in range(
                        human_attributes.pyridoxine_vitamin_B6_in_mg - 0.4,
                        human_attributes.pyridoxine_vitamin_B6_in_mg + 0.4) and nutrition_data.pantothenic_acid_vitamin_B3_in_mg in range(
                        human_attributes.pantothenic_acid_vitamin_B3_in_mg - 2.5,
                        human_attributes.pantothenic_acid_vitamin_B3_in_mg + 2.5) and nutrition_data.folacin_acid_vitamin_B9_in_mcg in range(
                        human_attributes.folacin_acid_vitamin_B9_in_mcg - 30,
                        human_attributes.folacin_acid_vitamin_B9_in_mcg + 30) and nutrition_data.cobalamin_acid_vitamin_B12_in_mcg in range(
                        human_attributes.cobalamin_acid_vitamin_B12_in_mcg - 2,
                        human_attributes.cobalamin_acid_vitamin_B12_in_mcg + 2) and nutrition_data.niacin_vitamin_PP_in_mg in range(
                        human_attributes.niacin_vitamin_PP_in_mg - 6,
                        human_attributes.niacin_vitamin_PP_in_mg + 6) and nutrition_data.ascorbic_acid_vitamin_C_in_mg in range(
                        human_attributes.ascorbic_acid_vitamin_C_in_mg - 15,
                        human_attributes.ascorbic_acid_vitamin_C_in_mg + 15) and nutrition_data.retinol_vitamin_A_in_mcg in range(
                        human_attributes.retinol_vitamin_A_in_mcg - 100,
                        human_attributes.retinol_vitamin_A_in_mcg + 100) and nutrition_data.tocopherol_vitamin_E_in_mg in range(
                        human_attributes.tocopherol_vitamin_E_in_mg - 1,
                        human_attributes.tocopherol_vitamin_E_in_mg + 1) and nutrition_data.cholecalciferol_vitamin_D_in_mcg in range(
                        human_attributes.cholecalciferol_vitamin_D_in_mcg - 1.1,
                        human_attributes.cholecalciferol_vitamin_D_in_mcg + 1.1) and nutrition_data.energy_value_in_kcal in range(
                        human_attributes.energy_value_in_kcal - 350, human_attributes.energy_value_in_kcal + 350):
                    is_correct = True
    return is_correct
