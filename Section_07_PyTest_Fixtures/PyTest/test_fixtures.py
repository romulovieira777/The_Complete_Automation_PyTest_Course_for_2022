import pytest


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    assert some_data == 42


@pytest.fixture()
def some_other_data():
    x = 43
    assert x == 42
    return x


def test_some_other_data(some_other_data):
    assert some_other_data == 42


@pytest.fixture()
def a_tuple():
    return 1, 'xoo', None, {'ch': 23}


def test_a_tuple(a_tuple):
    assert a_tuple[3]['ch'] == 32
