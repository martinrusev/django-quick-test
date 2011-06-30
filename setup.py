from setuptools import setup, find_packages
 
version = '0.3.0'
 
setup(
    name='django_quick_test',
    version='0.3.0',
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
    url='https://github.com/martinrusev/django-quick-test',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools','nose',],
    include_package_data=True,
) 
