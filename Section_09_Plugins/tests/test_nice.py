"""
Created on April 24, 2023

@author: Romulo
"""
import pytest


def test_fail(testdir):
    testdir.makepyfile("""
    def test_pass():
    assert 1 == 1
    
    def test_fail():
    assert 2 == 1   
    """)

    results = testdir.runpytest()
    results.stdout.fnmatch_lines(['*.F*', ])
    assert results.ret == 1


@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile(
        """
    def test_pass():
    assert 1 == 1
    
    def test_fail():
    assert 2 == 1   
    """
    )

    return testdir


def test_with_nice(sample_test):
    results = sample_test.runpytest('--nice')
    results.stdout.fnmatch_lines(['*.O*', ])
    assert results.ret == 1


def test_with_nice_verbose(sample_test):
    results = sample_test.runpytest('-v', '--nice')
    results.stdout.fnmatch_lines(['*::test_fail OPPORTUNITY for improvement*', ])
    assert results.ret == 1


def test_not_nice_verbose(sample_test):
    results = sample_test.runpytest('-v')
    results.stdout.fnmatch_lines(['*::test_fail FAILED*', ])
    assert results.ret == 1


def test_header(sample_test):
    results = sample_test.runpytest('--nice')
    results.stdout.fnmatch_lines(['Thanks for running the tests', ])


def test_header_not_nice(sample_test):
    results = sample_test.runpytest()
    thanks_message = 'Thanks for running the tests'
    assert thanks_message not in results.stdout.str()


def test_help_message(testdir):
    result = testdir.runpytest('--help')
    result.stdout.fnmatch_lines([
        'nice:',
        '*--nice*nice: Turn FAILED into OPPORTUNITY for improvement',
    ])
