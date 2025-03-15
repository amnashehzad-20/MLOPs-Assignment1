import pytest
from app.app import app, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def clear_tasks():
    tasks.clear()  # Clear tasks before each test
    yield
    tasks.clear()  # Clear tasks after each test

def test_index_get(client):
    """Test the index route with GET method."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Pomodoro To-Do List' in response.data

def test_index_post(client):
    """Test the index route with POST method."""
    response = client.post('/', data={'title': 'Test Task'})
    assert response.status_code == 200
    assert any(task['title'] == 'Test Task' for task in tasks)

def test_complete_task(client):
    """Test the complete_task route."""
    client.post('/', data={'title': 'Test Task'})
    task_id = tasks[0]['id']
    response = client.get(f'/complete/{task_id}')
    assert response.status_code == 302  # Redirect to index
    assert tasks[0]['completed'] is True

def test_empty_task_submission(client):
    """Test submitting an empty task."""
    initial_task_count = len(tasks)
    response = client.post('/', data={'title': ''})
    assert response.status_code == 200
    assert len(tasks) == initial_task_count  # No task should be added