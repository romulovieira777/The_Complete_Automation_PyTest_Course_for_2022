import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN a db with no tasks
    # WHEN a new task is added
    # THEN the returned id is valid
    new_task = Task('do something')
    task_id = tasks.add(new_task)

    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set(tasks_db):
    """Make sure the task_id field is set by tasks.add()."""
    # GIVEN a db with no tasks
    # WHEN a new task is added
    # THEN the task_id is set
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)
    task_from_db = tasks.get(task_id)

    assert task_from_db == task_id
    assert task_from_db[:-1] == task_id[:-1]


def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() affects tasks.count()."""
    # GIVEN a db with 3 tasks
    # WHEN another task is added
    # THEN tasks.count() returns 4
    tasks.add(Task('throw a party'))

    assert tasks.count() == 4
