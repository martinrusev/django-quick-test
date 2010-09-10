django-better-tests
=======================

This is a collection of commands for your django projects, that separates
test database creation from the actual test run


The advantages of using this over 'manage.py test' is that you can manually create 
the test database, run the test suite as many times as you wish without destroying it
and finally destroy the database or recreate it when they are changes in your application

------------
Installation
------------

1. Download the tarball and run ``python setup.py install``,

2. Add ``django_better_tests`` to your INSTALLED_APPS in settings.py:

       INSTALLED_APPS = (
		...
		'django_better_tests',
		...
		)


3. Add test database details in settings.py 

	DATABASES = {
		'default': {
			'ENGINE': '',
			
		},
		 'test': {
			'ENGINE': '',
			'NAME': 'test_database',
		}
	}		
	
		
4. That's it 
	   

-----
Usage
-----
Right now they are 3 commands in ``django_better_tests``: 


Create your test database with::

	python manage.py create_test_db 
	
After that run your tests with::

	python manage.py quick_test
	
And finally if you want destroy the test database with::

	python manage.py destroy_test_db
	
------------
Requirements
------------

Django 1.2+

