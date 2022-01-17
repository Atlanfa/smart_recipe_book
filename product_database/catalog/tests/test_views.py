from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.

from catalog.models import Product
from django.urls import reverse


class ProductListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 23 authors for pagination tests
        number_of_products = 23
        user = User.objects.create_user(username='testuser', password='12345')
        for product_num in range(number_of_products):
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

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/products/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('products'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('products'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/product_list.html')

    def test_pagination_is_twenty(self):
        resp = self.client.get(reverse('products'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['product_list']) == 20)

    def test_lists_all_products(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('products') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['product_list']) == 3)
