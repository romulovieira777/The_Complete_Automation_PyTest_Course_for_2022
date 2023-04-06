"""
Created on March 06, 2023

@author: Romulo
"""
import warnings
import pytest


def lame_fucntion():
    warnings.warn("Please stop using this", DeprecationWarning)


def test_lame_function():
    lame_fucntion()
    assert len(recwarn) == 1
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == "Please stop using this"


def test_lame_function_2():
    with pytest.warns(None) as warning_list:
        lame_fucntion()
    assert len(warning_list) == 1
    w = warning_list.pop()

    assert w.category == DeprecationWarning
    assert str(w.message) == "Please stop using this"
