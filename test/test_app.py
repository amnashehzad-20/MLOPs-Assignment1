import pytest
from app.app import app, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

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