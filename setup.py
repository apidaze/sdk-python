#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = None
with open('apidaze/__init__.py') as f:
    exec(f.read())

print(find_packages())

setup(
  name='apidaze',
  version=__version__,
  description='Python bindings for the APIdaze API',
  author='Apidaze',
  author_email='support@apidaze.com',
  keywords='cpaas telecommunication call sms api',
  url='https://github.com/apidaze/apidaze-python',
  packages=find_packages(),
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Communications :: Telephony',
  ],
)
