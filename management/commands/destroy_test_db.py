from django.core.management.base import BaseCommand
from optparse import make_option
import sys
from django.db import connection
from django.conf import settings

class Command(BaseCommand):
    help = 'Destroys the test db'


    def handle(self, *args, **options):
        test_db = settings.DATABASES['default']['NAME']
        connection.creation.destroy_test_db(test_db, verbosity = 1)        
    