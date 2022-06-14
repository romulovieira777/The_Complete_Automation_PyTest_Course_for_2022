"""
Created on June 14, 2022

@author romulo
"""
import time
from collections import namedtuple


Dinner = namedtuple('Dinner', ['food', 'cook', 'ready', 'id'])
Dinner.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    t_Dinner = Dinner('potatoes', 'Peter', True, 34)
    t_dict = t_Dinner._asdict()
    expected = {'food': 'potatoes', 'cook': 'Peter', 'ready': True, 'id': 34}
    assert t_dict == expected


def test_replace():
    time.sleep(0.1)
    t_before = Dinner('meat', 'Sam', False)
    t_after = t_before._replace(id=10, ready=True)
    t_expected = Dinner('meat', 'Mike', True, 10)
    assert t_after == t_expected
