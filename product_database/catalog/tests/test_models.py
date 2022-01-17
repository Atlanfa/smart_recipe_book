from django.contrib.auth.models import User
from django.test import TestCase

from catalog.models import Product

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        user = User.objects.create_user(username='testuser', password='12345')
        Product.objects.create(name='testproduct',
                               weight=10,
                               unit="Kilogram",
                               who_added=user,
                               product_by_weight_in_packaging='Yes',
                               proteins_in_100_g=100.0,
                               proteins_in_100_g_including_animals=100.0,
                               fat_in_100_g=100.0,
                               fat_in_100_g_including_animals=100.0,
                               digestible_carbohydrates_in_100_g=100.0,
                               digestible_carbohydrates_in_100_g_incl_m_and_d=100.0,
                               dietary_fiber_in_100_g=100.0,
                               dietary_fiber_in_100_g_including_fiber_and_pectin=100.0,
                               polyunsaturated_acid=100.0,
                               saturated_acid=100.0,
                               monounsaturated_acid=100.0,
                               calcium_in_100_g_in_mg=100.0,
                               phosphorus_in_100_g_in_mg=100.0,
                               magnesium_in_100_g_in_mg=100.0,
                               potassium_in_100_g_in_mg=100.0,
                               sodium_in_100_g_in_mg=100.0,
                               chlorine_in_100_g_in_mg=100.0,
                               sulfur_in_100_g_in_mg=100.0,
                               iron_in_100_g_in_mg=100.0,
                               zinc_in_100_g_in_mg=100.0,
                               iodine_in_100_g_in_mg=100.0,
                               fluorine_in_100_g_in_mg=100.0,
                               thiamine_vitamin_B1_in_100_g_in_mg=100.0,
                               riboflavin_vitamin_B2_in_100_g_in_mg=100.0,
                               pyridoxine_vitamin_B6_in_100_g_in_mg=100.0,
                               pantothenic_acid_vitamin_B3_in_100_g_in_mg=100.0,
                               folacin_acid_vitamin_B9_in_100_g_in_mcg=100.0,
                               cobalamin_acid_vitamin_B12_in_100_g_in_mcg=100.0,
                               niacin_vitamin_PP_in_100_g_in_mg=100.0,
                               ascorbic_acid_vitamin_C_in_100_g_in_mg=100.0,
                               retinol_vitamin_A_in_100_g_in_mcg=100.0,
                               tocopherol_vitamin_E_in_100_g_in_mg=100.0,
                               cholecalciferol_vitamin_D_in_100_g_in_mcg=100.0,
                               energy_value_in_kcal=100.0,
                               )

    def test_name_label(self):
        product=Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_weight_label(self):
        product=Product.objects.get(id=1)
        field_label = product._meta.get_field('weight').verbose_name
        self.assertEquals(field_label,'weight')

    def test_name_max_length(self):
        product=Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length,200)


    def test_get_absolute_url(self):
        product=Product.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(product.get_absolute_url(),'/catalog/product/1')
