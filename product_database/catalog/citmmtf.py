from .cdn import calculate_nutrition_for_menu_for_one_day
from datetime import datetime


def check_if_the_menu_matches_the_formula(menu_for_one_day, bnf, user_data):
    nutrition_data = calculate_nutrition_for_menu_for_one_day(menu_for_one_day)
    age = [datetime.now().year - user_data.date_of_birth.year] if (datetime.now().year - user_data.date_of_birth.year) > 1 else [datetime.datetime.now().month - user_data.date_of_birth.mount, 'm']
    is_correct = False
    for human_attributes in bnf.humans_attributes.all():

        demo = human_attributes.age
        age_choices = human_attributes.age[:-1].split('-').append('m') if 'm' in human_attributes.age else human_attributes.age.split('-')
        if 'm' in age_choices:
            if 'm' in age:
                if age[0] in range(int(age_choices[0]), int(age_choices[1])):
                        if (
                                human_attributes.proteins - 10 < nutrition_data.proteins < human_attributes.proteins +10000) and (
                                human_attributes.proteins_including_animals - 10 < nutrition_data.proteins_including_animals < human_attributes.proteins_including_animals +10000) and (
                                human_attributes.fat - 10 < nutrition_data.fat < human_attributes.fat +10000) and (
                                human_attributes.fat_including_animals - 10 < nutrition_data.fat_including_animals < human_attributes.fat_including_animals +10000) and (
                                human_attributes.digestible_carbohydrates - 30 < nutrition_data.digestible_carbohydrates < human_attributes.digestible_carbohydrates +10000) and (
                                human_attributes.digestible_carbohydrates_incl_m_and_d - 30 < nutrition_data.digestible_carbohydrates_incl_m_and_d < human_attributes.digestible_carbohydrates_incl_m_and_d +10000) and (
                                human_attributes.dietary_fiber - 4 < nutrition_data.dietary_fiber < human_attributes.dietary_fiber +10000) and (
                                human_attributes.dietary_fiber_including_fiber_and_pectin - 4 < nutrition_data.dietary_fiber_including_fiber_and_pectin < human_attributes.dietary_fiber_including_fiber_and_pectin +10000) and (
                                human_attributes.polyunsaturated_acid - 3 < nutrition_data.polyunsaturated_acid < human_attributes.polyunsaturated_acid +10000) and (
                                human_attributes.saturated_acid - 5 < nutrition_data.saturated_acid < human_attributes.saturated_acid +10000) and (
                                human_attributes.monounsaturated_acid - 6 < nutrition_data.monounsaturated_acid < human_attributes.monounsaturated_acid +10000) and (
                                human_attributes.calcium_in_mg - 90 < nutrition_data.calcium_in_mg < human_attributes.calcium_in_mg +10000) and (
                                human_attributes.phosphorus_in_mg - 100 < nutrition_data.phosphorus_in_mg < human_attributes.phosphorus_in_mg +10000) and (
                                human_attributes.magnesium_in_mg - 60 < nutrition_data.magnesium_in_mg < human_attributes.magnesium_in_mg +10000) and (
                                human_attributes.potassium_in_mg - 1000 < nutrition_data.potassium_in_mg < human_attributes.potassium_in_mg +10000) and (
                                human_attributes.sodium_in_mg - 900 < nutrition_data.sodium_in_mg < human_attributes.sodium_in_mg +10000) and (
                                human_attributes.chlorine_in_mg - 100 < nutrition_data.chlorine_in_mg < human_attributes.chlorine_in_mg +10000) and (
                                human_attributes.sulfur_in_mg - 200 < nutrition_data.sulfur_in_mg < human_attributes.sulfur_in_mg +10000) and (
                                human_attributes.iron_in_mg - 4 < nutrition_data.iron_in_mg < human_attributes.iron_in_mg +10000) and (
                                human_attributes.zinc_in_mg - 3 < nutrition_data.zinc_in_mg < human_attributes.zinc_in_mg +10000) and (
                                human_attributes.iodine_in_mg - 0.4 < nutrition_data.iodine_in_mg < human_attributes.iodine_in_mg +10000.4) and (
                                human_attributes.fluorine_in_mg - 2 < nutrition_data.fluorine_in_mg < human_attributes.fluorine_in_mg +10000) and (
                                human_attributes.thiamine_vitamin_B1_in_mg - 0.6 < nutrition_data.thiamine_vitamin_B1_in_mg < human_attributes.thiamine_vitamin_B1_in_mg +10000.6) and (
                                human_attributes.riboflavin_vitamin_B2_in_mg - 0.7 < nutrition_data.riboflavin_vitamin_B2_in_mg < human_attributes.riboflavin_vitamin_B2_in_mg +10000.7) and (
                                human_attributes.pyridoxine_vitamin_B6_in_mg - 0.4 < nutrition_data.pyridoxine_vitamin_B6_in_mg < human_attributes.pyridoxine_vitamin_B6_in_mg +10000.4) and (
                                human_attributes.pantothenic_acid_vitamin_B3_in_mg - 2.5 < nutrition_data.pantothenic_acid_vitamin_B3_in_mg < human_attributes.pantothenic_acid_vitamin_B3_in_mg +10000.5) and (
                                human_attributes.folacin_acid_vitamin_B9_in_mcg - 30 < nutrition_data.folacin_acid_vitamin_B9_in_mcg < human_attributes.folacin_acid_vitamin_B9_in_mcg +10000) and (
                                human_attributes.cobalamin_acid_vitamin_B12_in_mcg - 2 < nutrition_data.cobalamin_acid_vitamin_B12_in_mcg < human_attributes.cobalamin_acid_vitamin_B12_in_mcg +10000) and (
                                human_attributes.niacin_vitamin_PP_in_mg - 6 < nutrition_data.niacin_vitamin_PP_in_mg < human_attributes.niacin_vitamin_PP_in_mg +10000) and (
                                human_attributes.ascorbic_acid_vitamin_C_in_mg - 15 < nutrition_data.ascorbic_acid_vitamin_C_in_mg < human_attributes.ascorbic_acid_vitamin_C_in_mg +10000) and (
                                human_attributes.retinol_vitamin_A_in_mcg - 100 < nutrition_data.retinol_vitamin_A_in_mcg < human_attributes.retinol_vitamin_A_in_mcg +10000) and (
                                human_attributes.tocopherol_vitamin_E_in_mg - 1 < nutrition_data.tocopherol_vitamin_E_in_mg < human_attributes.tocopherol_vitamin_E_in_mg +10000) and (
                                human_attributes.cholecalciferol_vitamin_D_in_mcg - 1.1 < nutrition_data.cholecalciferol_vitamin_D_in_mcg < human_attributes.cholecalciferol_vitamin_D_in_mcg +10000.1) and (
                                human_attributes.energy_value_in_kcal - 350 < nutrition_data.energy_value_in_kcal < human_attributes.energy_value_in_kcal +10000):
                                is_correct = True
        else:
            if int(age_choices[0])<age[0]<int(age_choices[1]):
                print('calculating')
                print( human_attributes.proteins - 10000 < nutrition_data.proteins < human_attributes.proteins + 10000)
                print(human_attributes.proteins)
                print(nutrition_data.proteins)
                if (
                        human_attributes.proteins - 10000 < nutrition_data.proteins < human_attributes.proteins + 10000) and (
                        human_attributes.proteins_including_animals - 10000 < nutrition_data.proteins_including_animals < human_attributes.proteins_including_animals + 10000) and (
                        human_attributes.fat - 10000 < nutrition_data.fat < human_attributes.fat + 10000) and (
                        human_attributes.fat_including_animals - 10000 < nutrition_data.fat_including_animals < human_attributes.fat_including_animals + 10000) and (
                        human_attributes.digestible_carbohydrates - 10000<nutrition_data.digestible_carbohydrates < human_attributes.digestible_carbohydrates +10000) and (human_attributes.digestible_carbohydrates_incl_m_and_d -10000 < nutrition_data.digestible_carbohydrates_incl_m_and_d < human_attributes.digestible_carbohydrates_incl_m_and_d +10000) and (
                        human_attributes.dietary_fiber - 10000 < nutrition_data.dietary_fiber < human_attributes.dietary_fiber + 10000) and (
                        human_attributes.dietary_fiber_including_fiber_and_pectin - 10000<nutrition_data.dietary_fiber_including_fiber_and_pectin < human_attributes.dietary_fiber_including_fiber_and_pectin +10000) and (
                        human_attributes.polyunsaturated_acid - 10000 < nutrition_data.polyunsaturated_acid < human_attributes.polyunsaturated_acid + 10000) and (
                        human_attributes.saturated_acid - 10000 < nutrition_data.saturated_acid < human_attributes.saturated_acid + 10000) and (
                                human_attributes.monounsaturated_acid - 10000 < nutrition_data.monounsaturated_acid < human_attributes.monounsaturated_acid + 10000) and (
                                human_attributes.calcium_in_mg - 10000 < nutrition_data.calcium_in_mg < human_attributes.calcium_in_mg + 10000) and (
                                human_attributes.phosphorus_in_mg - 10000 < nutrition_data.phosphorus_in_mg < human_attributes.phosphorus_in_mg + 10000) and (
                                human_attributes.magnesium_in_mg - 10000 < nutrition_data.magnesium_in_mg < human_attributes.magnesium_in_mg + 10000) and (
                                human_attributes.potassium_in_mg - 10000 < nutrition_data.potassium_in_mg < human_attributes.potassium_in_mg + 10000) and (
                                human_attributes.sodium_in_mg - 10000 < nutrition_data.sodium_in_mg < human_attributes.sodium_in_mg + 10000) and (
                                human_attributes.chlorine_in_mg - 10000 < nutrition_data.chlorine_in_mg < human_attributes.chlorine_in_mg + 10000) and (
                                human_attributes.sulfur_in_mg - 10000 < nutrition_data.sulfur_in_mg < human_attributes.sulfur_in_mg + 10000) and (
                                human_attributes.iron_in_mg - 10000 < nutrition_data.iron_in_mg < human_attributes.iron_in_mg + 10000) and (
                                human_attributes.zinc_in_mg - 10000 < nutrition_data.zinc_in_mg < human_attributes.zinc_in_mg + 10000) and (
                                human_attributes.iodine_in_mg - 10000.4 < nutrition_data.iodine_in_mg < human_attributes.iodine_in_mg + 10000.4) and (
                                human_attributes.fluorine_in_mg - 10000 < nutrition_data.fluorine_in_mg < human_attributes.fluorine_in_mg + 10000) and (
                                human_attributes.thiamine_vitamin_B1_in_mg - 10000.6 < nutrition_data.thiamine_vitamin_B1_in_mg < human_attributes.thiamine_vitamin_B1_in_mg + 10000.6) and (
                                human_attributes.riboflavin_vitamin_B2_in_mg - 10000.7 < nutrition_data.riboflavin_vitamin_B2_in_mg < human_attributes.riboflavin_vitamin_B2_in_mg + 10000.7) and (
                                human_attributes.pyridoxine_vitamin_B6_in_mg - 10000.4 < nutrition_data.pyridoxine_vitamin_B6_in_mg < human_attributes.pyridoxine_vitamin_B6_in_mg + 10000.4) and (
                                human_attributes.pantothenic_acid_vitamin_B3_in_mg - 10000.5 < nutrition_data.pantothenic_acid_vitamin_B3_in_mg < human_attributes.pantothenic_acid_vitamin_B3_in_mg + 10000.5) and (
                                human_attributes.folacin_acid_vitamin_B9_in_mcg - 10000 < nutrition_data.folacin_acid_vitamin_B9_in_mcg < human_attributes.folacin_acid_vitamin_B9_in_mcg + 10000) and (
                                human_attributes.cobalamin_acid_vitamin_B12_in_mcg - 10000 < nutrition_data.cobalamin_acid_vitamin_B12_in_mcg < human_attributes.cobalamin_acid_vitamin_B12_in_mcg + 10000) and (
                                human_attributes.niacin_vitamin_PP_in_mg - 10000 < nutrition_data.niacin_vitamin_PP_in_mg < human_attributes.niacin_vitamin_PP_in_mg + 10000) and (
                                human_attributes.ascorbic_acid_vitamin_C_in_mg - 10000 < nutrition_data.ascorbic_acid_vitamin_C_in_mg < human_attributes.ascorbic_acid_vitamin_C_in_mg + 10000) and (
                                human_attributes.retinol_vitamin_A_in_mcg - 10000 < nutrition_data.retinol_vitamin_A_in_mcg < human_attributes.retinol_vitamin_A_in_mcg + 10000) and (
                                human_attributes.tocopherol_vitamin_E_in_mg - 10000 < nutrition_data.tocopherol_vitamin_E_in_mg < human_attributes.tocopherol_vitamin_E_in_mg + 10000) and (
                                human_attributes.cholecalciferol_vitamin_D_in_mcg - 10000.1 < nutrition_data.cholecalciferol_vitamin_D_in_mcg < human_attributes.cholecalciferol_vitamin_D_in_mcg + 10000.1) and (
                                human_attributes.energy_value_in_kcal - 10000 < nutrition_data.energy_value_in_kcal < human_attributes.energy_value_in_kcal + 10000):

                    print('SUCCESS')
                    is_correct = True
                    break
                print('done calculating')
    print(f'here {is_correct}')
    return is_correct



