from django.core.management.base import BaseCommand
from optparse import make_option
import sys
from django.db import connection
from django.conf import settings
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Creates the test db'

    def handle(self, *args, **options):
        connection.creation.create_test_db(verbosity = 1, autoclobber=False)
        call_command('migrate', database='test', app=None, 
                     target=None, skip=False, merge=False, backwards=False, fake=False, db_dry_run=False, show_list=False)
        
        connection.close()
        
    