import os
import sys
from django.conf import settings
from django.core.management.base import BaseCommand
from django.test.simple import DjangoTestSuiteRunner
import nose.core
from plugin import ResultPlugin
from django.db.backends import creation
from django.db import connection, DatabaseError

try:
	any
except NameError:
	def any(iterable):
		for element in iterable:
			if element:
				return True
		return False

# This is a table of Django's "manage.py test" options which
# correspond to nosetests options with a different name:
OPTION_TRANSLATION = {'--failfast': '-x'}


class NoseTestSuiteRunner(DjangoTestSuiteRunner):

	def run_suite(self, nose_argv):
		result_plugin = ResultPlugin()
		nose.core.TestProgram(argv=nose_argv, exit=False,
				addplugins=[result_plugin])
		return result_plugin.result

	def run_tests(self, test_labels, extra_tests=None):
		"""
		Run the unit tests for all the test names in the provided list.

		Test names specified may be file or module names, and may optionally
		indicate the test case to run by separating the module or file name
		from the test case name with a colon. Filenames may be relative or
		absolute.  Examples:

		runner.run_tests('test.module')
		runner.run_tests('another.test:TestCase.test_method')
		runner.run_tests('a.test:TestCase')
		runner.run_tests('/path/to/test/file.py:test_function')

		Returns the number of tests that failed.
		"""

		settings.DEBUG = False

		self.setup_test_environment()
		
		
		# Switch to the test database
		old_name = settings.DATABASES['default']['NAME']

		if settings.DATABASES['test']['NAME']:
			settings.DATABASES['default']['NAME'] = settings.DATABASES['test']['NAME']
		else:
			settings.DATABASES['default']['NAME'] = creation.TEST_DATABASE_PREFIX + settings.DATABASES['default']['NAME']
		
		connection.settings_dict["DATABASE_NAME"] = settings.DATABASES['default']['NAME']
	
		try:
			settings.DATABASES['default']['SUPPORTS_TRANSACTIONS'] = connection.creation._rollback_works()	
		except: 
			pass

		nose_argv = ['nosetests', '--verbosity', str(self.verbosity)]

		if hasattr(settings, 'NOSE_ARGS'):
			nose_argv.extend(settings.NOSE_ARGS)

		# Skip over 'manage.py test' and any arguments handled by django.
		django_opts = ['--noinput']
		for opt in BaseCommand.option_list:
			django_opts.extend(opt._long_opts)
			django_opts.extend(opt._short_opts)

		nose_argv.extend(OPTION_TRANSLATION.get(opt, opt)
				for opt in sys.argv[2:]
				if not any(opt.startswith(d) for d in django_opts))

		if self.verbosity >= 1:
			print ' '.join(nose_argv)


		result = self.run_suite(nose_argv)

		#Restore the old db name.
		settings.DATABASES['default']['NAME'] = old_name
		connection.settings_dict["DATABASE_NAME"] = old_name

		self.teardown_test_environment()
		# suite_result expects the suite as the first argument.  Fake it.
		return self.suite_result({}, result)


def _get_options():
	"""Return all nose options that don't conflict with django options."""
	cfg_files = nose.core.all_config_files()
	manager = nose.core.DefaultPluginManager()
	config = nose.core.Config(env=os.environ, files=cfg_files, plugins=manager)
	options = config.getParser().option_list
	django_opts = [opt.dest for opt in BaseCommand.option_list] + ['version']
	return tuple(o for o in options if o.dest not in django_opts and
			o.action != 'help')


# Replace the builtin command options with the merged django/nose options.
NoseTestSuiteRunner.options = _get_options()
NoseTestSuiteRunner.__test__ = False
