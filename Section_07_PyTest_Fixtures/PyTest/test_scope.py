import pytest


@pytest.fixture(scope='function')
def func_scope():
    """some data"""
    print('\nSetup func_scope')
    yield
    print('\nTeardown func_scope')


@pytest.fixture(scope='module')
def mod_scope():
    """some data"""
    print('\nSetup mod_scope')
    yield
    print('\nTeardown mod_scope')


@pytest.fixture(scope='session')
def sess_scope():
    """some data"""
    print('\nSetup sess_scope')
    yield
    print('\nTeardown sess_scope')


@pytest.fixture(scope='class')
def class_scope():
    """some data"""
    print('\nSetup class_scope')
    yield
    print('\nTeardown class_scope')


def test_1(sess_scope, mod_scope, func_scope):
    """some data"""
    print('\nRunning test_1()')


def test_2(sess_scope, mod_scope, func_scope):
    """some data"""
    print('\nRunning test_2()')


@pytest.mark.usefixtures('class_scope')
class TestClassScope:
    def test_3(self):
        """some data"""
        print('\nRunning test_3()')

    def test_4(self):
        """some data"""
        print('\nRunning test_4()')
