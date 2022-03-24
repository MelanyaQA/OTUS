import requests
import pytest


def test_all_resource():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(response.text)


def test_post_resource():
    data = {'userId': '11', 'id': '101', 'title': 'by Melanya', 'body': 'new test2'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data)
    print(response.text)


@pytest.mark.parametrize('userId', [1, 2, 3])
def test_resource_param(userId):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts?{userId}')
    print(response.text)
    assert response.status_code == 200


def test_33():
    r = requests.get('https://jsonplaceholder.typicode.com/posts/33')
    print(r.text)







