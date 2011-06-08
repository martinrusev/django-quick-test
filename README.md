# django-better-tests


This is a collection of commands for your django projects, that separates
test database creation from the actual test run


The advantages of using this over 'manage.py test' is that you control both
the database creation and the test run


## Installation


1. Either download the tarball and run ``python setup.py install``,

2. Add ``django_better_tests`` to your INSTALLED_APPS in settings.py:


	INSTALLED_APPS = ('django_better_tests')



3. Add test database details in settings.py 


	DATABASES = {
		'default':{
			'ENGINE':''},
		'test':{
			'ENGINE': '',
			'NAME': 'test_database',
		}
	}		


4. Then set TEST_RUNNER in settings.py:

	TEST_RUNNER = 'django_better_tests.NoseTestSuiteRunner'



## Usage


Once installed, using the new test suite runner replacement is easy. Create your test database with::

	python manage.py create_test_db 

After that run your tests with

	python manage.py quick_test


And finally if you want destroy the test database with

	python manage.py destroy_test_db



## Alternative usage 


You can use just the quick_test command and manualy update the database only when needed. 

Manual commands

	python manage.py syncdb --database=test
	python manage.py migrate --database=test

and after that only

	python manage.py quick_test



## Requirements


Django 1.2+

nose

