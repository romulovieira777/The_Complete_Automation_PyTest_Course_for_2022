"""
Created on March 03, 2023

@author: Romulo
"""


def pytest_addoption(parser):
    parser.addoption("--myenv", action="store", help="some bool option")
    parser.addoption("--foo", action="store", default="bar", help="foo: bar or baz")
