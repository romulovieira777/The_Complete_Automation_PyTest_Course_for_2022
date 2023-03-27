import pytest


@pytest.fixture(name='felicity')
def answer_of_the_answers_forever():
    return 42


def test_answer(felicity):
    assert felicity == 42
