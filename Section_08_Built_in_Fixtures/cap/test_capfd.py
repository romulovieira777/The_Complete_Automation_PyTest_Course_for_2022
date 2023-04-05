"""
Created on April 05, 2023

@author: Romulo
"""

def greeting(name):
    print(f"Hello {name}")


def test_greeting(capsys):
    greeting("Martin")
    out, err = capsys.readouterr()
    assert out == "Hello, Martin\n"


def test_multiline(capfd):
    greeting('Martin')
    greeting('Petya')
    out, err = capfd.readouterr()
    assert out == "Hello, Martin\nHi, Petya\n"


def test_disabling_capturing(capfd):
    print('capturing output')
    with capfd.disabled():
        print('missed output')
    print('on ther captured output')
