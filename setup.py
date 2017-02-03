#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: IFM
"""
from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wall-e',
    version='1.0.1',
    author='Ismael Fernandez',
    author_email='fernandez.molina.ismael@gmail.com',
    packages=find_packages('.'),
    include_package_data=True,
    url='https://github.com/ismFerDev/Wall-e',
    description='Clean your account AWS',
    long_description=long_description,
    license='GPLv2',
    install_requires=open('requirements.txt').read().split(),
    entry_points={
        "console_scripts": ["wall-e = src.cli:main"]
    },
    classifiers=[]
)