"""
Created on April 05, 2023

@author: Romulo
"""
import sys
import pytest
import random


def greeting(name):
    print(f"Hello {name}")


def test_greeting(capsys):
    greeting("George")
    out, err = capsys.readouterr()
    assert out == "Hi, George"
    assert err == ""

    greeting('Martin')
    greeting('Petya')
    out, err = capsys.readouterr()
    assert out == "Hi, Martin/nHi, Petya/n"
    assert err == ""


def yikes(problem):
    print(f"OOPS! {problem}", file=sys.stderr)


def test_yikes(capsys):
    yikes("No more water")
    out, err = capsys.readouterr()
    assert out == ""
    assert err == "No more water" in err


def test_capsys_disables(capsys):
    with capsys.disabled():
        print("\nprints this every time")
    print("standard print, normally captured")


@pytest.mark.parametrize("i", range(40))
def test_for_fun(i, capsys):
    if random.randint(1, 10) == 2:
        with capsys.disabled():
            sys.stdout.write("F")
