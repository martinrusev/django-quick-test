=================
django-quick-test
=================

Django quick test is a custom nose based test runner that
separates testing and test related database manipulations.


Usualy running this command instead of the default ``manage.py test``
will give you 10-15 times speed boost. So you will be able to run
your test suite in seconds instead of minutes.

===============
 Installation
===============


1. Install the package with ``pip install django_quick_test`` or alternatively you can  
download the tarball and run ``python setup.py install``

2. Add ``quick_test`` to your INSTALLED_APPS list in settings.py
   

::

	INSTALLED_APPS = ('quick_test')



3. Add your test database details in settings.py 

::

	DATABASES = {
		'default':{
			'ENGINE':''},
		'test':{
			'ENGINE': '',
			'NAME': 'test_database',
		}
	}		


4. And finally replace the default Django test runner with this one. Again in settings.py:

::

	TEST_RUNNER = 'quick_test.testrunner.NoseTestSuiteRunner'


=========
 Usage 
=========

django-quick-test assumes that you have created your test database manualy and 
you have loaded the required test data(fixtures) 



Commands you have to run before using the command

::

	python manage.py syncdb --database=test
	python manage.py migrate --database=test


and finaly run your tests with

::

	python manage.py quick_test


==================
 Additional notes
==================


If you are using the default Django TestCase class
you have to ovewrite the ``_pre_setup`` method which is executed
automatically when you call the class. If you don't overwrite it
the ``quick_test`` command will still work, but your test data
will be lost. Even if you don't have any fixtures in the database
overwriting this method will give you additional speed boost.

::

    from django.test import TestCase

    class SimpleTest(TestCase)

	    def _pre_setup(self):
		    # this method flushes the database and installs 
		    # the fixtures defined in the fixtures=[] list
		    # we are doing everything manually, so we don't
		    # really need it
            
            # these are the results I get with 1 test before
            and after ovewriting the method
            # Before -> Ran 1 test in 2.336s
            # After -> Ran 1 test in 0.004s 
		    pass

	    def test_basic_addition(self):
		    self.assertEqual(1 + 1, 2)
 


===============
 Requirements
===============


Django 1.2+

nose

