# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='sample',
    version='0.1.0',
    description='igata for Python',
    long_description=readme,
    author='Yuki Yoshida',
    author_email='yuki.yoshida@access-company.com',
    url='https://github.com/aYukiYoshida/pyigata',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=install_requires
)
