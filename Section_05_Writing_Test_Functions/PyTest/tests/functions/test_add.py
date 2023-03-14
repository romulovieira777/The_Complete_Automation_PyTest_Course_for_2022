'''
Created on Mar 13, 2023

@author: Romulo
'''

import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id():
    new_task = Task('take action')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    new_task = Task('get food', owner='me', done=True)
    task_id = tasks.add(new_task)

    task_from_db = tasks.get(task_id)

    assert task_from_db.id == task_id
    

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
   
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield
    tasks.stop_tasks_db()
