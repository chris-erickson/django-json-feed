import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-json-feed',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Implement JSON feeds in Django using the syndication framework.',
    long_description='Implement JSON feeds in Django using the syndication framework that conform to the JSON Feed standard.',
    url='https://github.com/chris-erickson/django-json-feed',
    author='Chris Erickson',
    author_email='chris+django-json-feed@groundedwing.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
