from django.test import TestCase

from catalog.forms import RenewProductForm

class RenewProductFormTest(TestCase):

    def test_renew_form_name_field_label(self):
        form = RenewProductForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'name')

    def test_renew_form_name_field_help_text(self):
        form = RenewProductForm()
        self.assertEqual(form.fields['name'].help_text,'Enter product name')

