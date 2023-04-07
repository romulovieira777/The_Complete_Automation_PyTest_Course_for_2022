"""
Created on April 07, 2023

@author: Romulo
"""
from setuptools import setup

setup(
    name='pytest-nice',
    version='0.1.0',
    description='A plugin to make the FAILURE into OPPORTUNITY',
    url='skilledarmy.com',
    author='Romulo',
    author_email='teste@gmail.com',
    license='myproperty',
    py_modules=['pytest_nice'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['nice = pytest_nice']},
)
