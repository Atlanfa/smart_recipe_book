from catalog.regions import get_regions
from catalog.data_dict import data
from catalog.models import BalancedNutritionFormula
from catalog.human_attributes_template import create_templates


def create_regions():
    for country in get_regions(data):
        bnf = BalancedNutritionFormula.objects.create(country=country)
        humans_attributes = create_templates()
        for human_attribute in humans_attributes:
            human_attribute.related_model = bnf
            human_attribute.save()
        bnf.humans_attributes.set(humans_attributes)
        bnf.save()

