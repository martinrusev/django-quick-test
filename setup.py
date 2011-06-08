from setuptools import setup, find_packages
 
version = '0.2.0'
 
setup(
    name='django_better_tests',
    version='0.2.0',
    description="Django test runner that separates test database creation and test running",
    long_description=open('README.rst').read(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django, tests, nose,',
    author='Martin Rusev',
    author_email='martinrusev@live.com',
    url='http://github.com/martinrusev/django-better-tests',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools','nose',],
    include_package_data=True,
    setup_requires=['setuptools_git'],
) 
