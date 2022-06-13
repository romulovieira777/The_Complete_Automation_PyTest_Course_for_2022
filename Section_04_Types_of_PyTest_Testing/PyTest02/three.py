"""
Created on June 13, 2022

@author romulo
"""
from collections import namedtuple


Dinner = namedtuple('Dinner', ['food', 'clock', 'ready', 'id'])
Dinner.__new__.__defaults__ == (None, None, False, None)


def test_defaults():
    t1 = Dinner()
    t2 = Dinner(None, None, False, None)
    assert t1 == t2


def test_num_access():
    t = Dinner('potatoes', 'Sam')
    assert t.food == 'potatoes'
    assert t.cook == 'Sam'
    assert (t.ready, t.id) == (False, None)
