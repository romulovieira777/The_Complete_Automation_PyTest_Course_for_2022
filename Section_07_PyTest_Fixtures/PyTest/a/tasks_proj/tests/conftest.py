import pytest
import tasks
from tasks import Task


@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield

    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Will', True),
        Task('Codi reviews Will code', 'Codi', False),
        Task('Fix Will code', 'Jess', False)
    )


@pytest.fixture()
def tasks_multi_per_owner():
    """Several owners with several tasks each, all with different names."""
    return (
        Task('Make a breakfast', 'Adam'),
        Task('Clean', 'Martin'),
        Task('Cook', 'Guillermo'),

        Task('Create', 'Pamela'),
        Task('Edit', 'Pamela'),
        Task('Copy', 'Pamela'),

        Task('Bake', 'Guillermo'),
        Task('Broil', 'Guillermo'),
        Task('Fry', 'Guillermo')
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_multi_per_owner):
    """Connected db with 9 tasks, 3 owners, all with 3 tasks."""
    for t in tasks_multi_per_owner:
        tasks.add(t)
