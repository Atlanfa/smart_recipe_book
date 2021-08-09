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
    ('f', 'Female'),
)

PAGS = (
    ('k', 'kid'),
    ('i', 'workers mostly mental work, very light physical activity'),
    ('ii', 'workers engaged in light work, light physical activity'),
    ('iii', 'workers of average hard work, average physical activity'),
    ('iv', 'workers of hard physical labor, high physical activity'),
    ('v', 'workers of especially heavy physical work, very high physical activity')
)

BIRTH_YEAR_CHOICES = [year for year in range(1900, (date.today().year + 1))]

KID_YEAR_LIST = ['0-3m', '4-6m', '7-12m', '1-3', '4-6', '6-student', '7-10', '11-13', '14-17']

YEAR_LIST = ['18-29', '30-39', '40-59', '60-74', '75-more']

WEIGHT = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
