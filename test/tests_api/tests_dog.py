import requests
import pytest


@pytest.mark.parametrize("breed", ['pitbull', 'koshka'], ids=['valid_value', 'negative'])
def test_breed(breed):
    url = f'https://dog.ceo/api/breed/{breed}/images'
    response = requests.get(url)
    print(response.text)
    print(response.status_code)



@pytest.mark.parametrize('random_breed', ['african', 'rottweiler'])
def test_random_breed(random_breed):
    url = f'https://dog.ceo/api/breed/{random_breed}/images/random'
    response = requests.get(url)
    assert response.status_code == 200


def test_all_dog():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    assert response.status_code == 200



def test_sub_breed():
    response = requests.get('https://dog.ceo/api/breed/hound/afghan/images')
    assert response.status_code == 200


def test_random_all_dog():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.status_code == 200
