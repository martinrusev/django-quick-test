from django.core.management.base import BaseCommand
from django.db import connections, connection
from django.conf import settings
import time


TEST_DATABASE_NAME = settings.DATABASES['test']['NAME']

class Command(BaseCommand):
	help = 'Destroys the test db'

	def handle(self, *args, **options):

		connection.close()
		if settings.DATABASES['default'] != "sqlite3":

			cursor = connections['default'].cursor() #connect to the real database to avoid 'cannot drop the currently open database'
			try:
				cursor.execute('commit')
			except AttributeError:
				pass
			else:
				time.sleep(2) # To avoid "database is being accessed by other users" errors.
				cursor.execute("DROP DATABASE %s" % TEST_DATABASE_NAME)

