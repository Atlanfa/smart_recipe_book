from catalog.choices import SEXES, YEAR_LIST, PAGS, WEIGHT, KID_YEAR_LIST
from catalog.models import HumanAttributes


def create_templates():
    attribute_list = []
    for year in KID_YEAR_LIST:
        attribute = HumanAttributes()
        attribute.age = year[-1]
        attribute.pag = PAGS[-1]
        if 'm' in year:
            attribute.weight = 1
            attribute.sex = 'Both'
        elif year in KID_YEAR_LIST[4:7]:
            attribute.sex = 'Both'
        attribute_list.append(attribute)
    for year in YEAR_LIST[:-2]:
        attribute = HumanAttributes()
        attribute.age = year[-1]
        for weight in WEIGHT:
            attribute.weight = weight
            for sex in SEXES:
                attribute.sex = sex[-1]
                for pag in PAGS[1:]:
                    attribute.pag = pag[-1]
        attribute_list.append(attribute)
    for year in YEAR_LIST[-2:]:
        attribute = HumanAttributes()
        attribute.age = year[-1]
        for sex in SEXES:
            attribute.sex = sex[-1]
        attribute_list.append(attribute)
    for human_attribute in attribute_list:
        human_attribute.age = YEAR_LIST[0][1]
        human_attribute.pag = PAGS[1][0]
        human_attribute.sex = SEXES[0][0]
        human_attribute.cpa = 1.4
        human_attribute.weight = 70
        human_attribute.proteins = 88
        human_attribute.proteins_including_animals = 48
        human_attribute.fat = 107
        human_attribute.fat_including_animals = 32
        human_attribute.digestible_carbohydrates = 422
        human_attribute.digestible_carbohydrates_incl_m_and_d = 75
        human_attribute.dietary_fiber = 22.5
        human_attribute.dietary_fiber_including_fiber_and_pectin = 12.5
        human_attribute.polyunsaturated_acid = 0
        human_attribute.saturated_acid = 0
        human_attribute.monounsaturated_acid = 0
        human_attribute.calcium_in_mg = 800
        human_attribute.phosphorus_in_mg = 1200
        human_attribute.magnesium_in_mg = 400
        human_attribute.potassium_in_mg = 3750
        human_attribute.sodium_in_mg = 5000
        human_attribute.chlorine_in_mg = 8500
        human_attribute.sulfur_in_mg = 1000
        human_attribute.iron_in_mg = 14
        human_attribute.zinc_in_mg = 15
        human_attribute.iodine_in_mg = 0.15
        human_attribute.fluorine_in_mg = 3
        human_attribute.thiamine_vitamin_B1_in_mg = 1.6
        human_attribute.riboflavin_vitamin_B2_in_mg = 1.8
        human_attribute.pyridoxine_vitamin_B6_in_mg = 1.9
        human_attribute.pantothenic_acid_vitamin_B3_in_mg = 12.5
        human_attribute.folacin_acid_vitamin_B9_in_mcg = 200
        human_attribute.cobalamin_acid_vitamin_B12_in_mcg = 3
        human_attribute.niacin_vitamin_PP_in_mg = 21
        human_attribute.ascorbic_acid_vitamin_C_in_mg = 85
        human_attribute.retinol_vitamin_A_in_mcg = 900
        human_attribute.tocopherol_vitamin_E_in_mg = 9
        human_attribute.cholecalciferol_vitamin_D_in_mcg = 2.5
        human_attribute.energy_value_in_kcal = 3000
    return attribute_list






