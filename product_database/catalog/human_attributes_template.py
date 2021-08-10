from choices import PAGS, KID_YEAR_LIST, WEIGHT, SEXES, YEAR_LIST
from models import HumanAttributes


def create_templates():
    attribute_list = []
    for year in KID_YEAR_LIST:
        attribute = HumanAttributes()
        attribute.age = year
        attribute.pga = 'k'
        if 'm' in year:
            attribute.weight = 1
            attribute.sex = 'Both'
        elif year in KID_YEAR_LIST[4:7]:
            attribute.sex = 'Both'
        attribute_list.append(attribute)
    for year in YEAR_LIST[:-2]:
        attribute.age = year
        for weight in WEIGHT:
            attribute.weight = weight
            for sex in SEXES:
                attribute.sex = sex[0]
                for pag in PAGS[1:]:
                    attribute.pag = pag[0]
        attribute_list.append(attribute)
    for year in YEAR_LIST[-2:]:
        attribute.age = year
        for sex in SEXES:
            attribute.sex = sex[0]








