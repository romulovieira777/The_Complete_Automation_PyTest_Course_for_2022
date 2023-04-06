"""
Created on March 06, 2023

@author: Romulo
"""
import os
import json


def read_cheese_performance():
    full_path = os.path.expanduser("~/cheese.json")

    with open(full_path, 'r') as f:
        prefs = json.load(f)
    return prefs


def write_cheese_preferences(prefs):
    full_path = os.path.expanduser("~/cheese.json")

    with open(full_path, 'w') as f:
        json.dump(prefs, f, indent=4)


def write_defould_cheese_preferences():
    write_cheese_preferences(_default_prefs)

_default_prefs = {
    'slicing': ['manchago', 'sharp'],
    'spreadable': ['Saint Andre', 'cambert', 'bucheron', 'goat', 'humbolt fog', 'cambozola'],
    'salads': ['crumbled feta']
}

if __name__ == '__main__':
    write_defould_cheese_preferences()
