from datetime import date

UNITS = (
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
        ('thing', 'Thing')
    )


SEXES = (
    ('m', 'Male'),
    ('f', 'Female')
)


CPAS = (
    ('i', 'workers mostly mental work, very light physical activity'),
    ('ii', 'workers engaged in light work, light physical activity'),
    ('iii', 'workers of average hard work, average physical activity'),
    ('iv', 'workers of hard physical labor, high physical activity'),
    ('v', 'workers of especially heavy physical work, very high physical activity')
)

BIRTH_YEAR_CHOICES = [year for year in range(1900, (date.today().year + 1))]
