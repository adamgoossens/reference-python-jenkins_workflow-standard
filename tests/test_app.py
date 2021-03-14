import pytest
from fruitandnut import app
import json

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def __assert_results(response, expected_names, expected_descriptions):
    names = [f['name'] for f in response]
    descriptions = [f['description'] for f in response]
    
    assert len(response) == len(expected_names) == len(expected_descriptions)
    assert sorted(expected_names) == sorted(names)
    assert sorted(expected_descriptions) == sorted(descriptions)

def test_list_fruits(client):
    expected_names = ['Banana', 'Apple']
    expected_descriptions = ['Tropical fruit', 'Winter fruit']

    rv = client.get('/fruits')
    __assert_results(rv.get_json(), expected_names, expected_descriptions)

def test_post_and_delete_fruit(client):
    expected_names = ['Banana', 'Apple', 'Pineapple']
    expected_descriptions = ['Tropical fruit', 'Winter fruit', 'Tropical fruit']

    rv = client.post('/fruits', data=json.dumps(dict(
        name='Pineapple',
        description='Tropical fruit')),
        content_type='application/json')

    assert rv.status_code == 200
    
    rv = client.get('/fruits')
    response = rv.get_json()
    __assert_results(rv.get_json(), expected_names, expected_descriptions)

    # delete pineapple
    expected_names = ['Banana', 'Apple']
    expected_descriptions = ['Tropical fruit', 'Winter fruit']
    rv = client.delete('/fruits', data=json.dumps(dict(
        name='Pineapple',
        description='Tropical fruit')),
        content_type='application/json')
    
    assert rv.status_code == 200

    rv = client.get('/fruits')
    __assert_results(rv.get_json(), expected_names, expected_descriptions)

