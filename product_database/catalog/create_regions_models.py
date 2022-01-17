from regions import get_regions
from data_dict import data
from models import BalancedNutritionFormula

for country in get_regions(data):
    BalancedNutritionFormula.objects.create(country=country)
