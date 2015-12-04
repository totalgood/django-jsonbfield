# from setuptools import find_packages
from distutils.core import setup


try:
    long_description = open('README.rst', 'r').read()
except:  # (IOError, ImportError, OSError, RuntimeError):
    long_description = ('The Postgres 9.4 JSONB field support coming in Django 1.9'
                        ' extracted to a standalone module')

setup(
    name='django-jsonbfield',
    version='0.1.0',
    description='Django JSONField that utilized PostGRESQL jsonb field type',
    long_description=long_description,
    author='Tome Cvitan',
    author_email='tome@cvitan.com',
    url='https://github.com/totalgood/django-jsonbfield/',
    # download_url='https://github.com/totalgood/django-jsonbfield/tarball/v0.1.2',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='django postgres jsonb',
    packages=['jsonbfield'],  # find_packages(exclude=['tests*']),
    install_requires=[
        'psycopg2>=2.5.4',
        'Django>=1.8'
    ]
)
