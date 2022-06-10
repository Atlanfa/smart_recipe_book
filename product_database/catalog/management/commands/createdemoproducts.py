from django.core.management.base import BaseCommand

from catalog.create_food_models import create_food


class Command(BaseCommand):
    help = 'Creates demo for food and stores and prices and kitchen utensils models'

    def handle(self, *args, **options):
        create_food()
        self.stdout.write(self.style.SUCCESS('Successfully added demo for food and stores and prices and kitchen utensils models'))
