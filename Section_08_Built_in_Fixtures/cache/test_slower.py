"""
Created on April 04, 2023

@author: Romulo
"""
import datetime
import pytest
import random
import time


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':', '_')
    start_time = datetime.datetime.now()

    yield

    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)

    if last_duration is not None:
        errormess = "When the time of execution is 2x the last execution"
        assert this_duration < last_duration * 2, errormess


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())
