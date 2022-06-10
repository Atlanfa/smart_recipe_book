from django.core.management.base import BaseCommand

from catalog.create_regions_models import create_regions


class Command(BaseCommand):
    help = 'Creates demo for regions balanced nutrition formulas models'

    def handle(self, *args, **options):
        create_regions()
        self.stdout.write(self.style.SUCCESS('Successfully added demo for regions balanced nutrition formulas models'))
