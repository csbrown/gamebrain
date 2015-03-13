#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='gamebrain',
      version='0.1',
      description='Game AI Library',
      author='Scott Brown',
      author_email='gitpushoriginmaster@gmail.com',
      packages=find_packages(),
      package_data={'' : ['data/*']},
      include_package_data=True,
     )
