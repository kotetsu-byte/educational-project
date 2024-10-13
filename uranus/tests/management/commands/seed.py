from django.core.management.base import BaseCommand
from models import Test

class Command(BaseCommand):
    help = 'Seeds the database with initial test data'

    def handle(self, *args, **kwargs):
        # C++
        