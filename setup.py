# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='splatoon_league_corr',
    version='1.0.0',
    description='Correlation Coefficient Table for Splatoon s League',
    long_description=readme,
    author='Maruyama Jumpei',
    author_email='jmp.mtywt.lv@gmail.com',
    url='https://github.com/JmpM-0743/splatoon_league_corr.git',
    license=license,
	install_requires = ['pandas','datetime','openpyxl'],
    packages=find_packages(exclude=('samples', 'docs'))
)

