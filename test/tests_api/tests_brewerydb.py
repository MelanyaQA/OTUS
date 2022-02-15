import pytest
import requests

@pytest.mark.parametrize('city', ['alameda', 'moscow', 'karaganda'], ids=['valid_value', 'valid_value', 'negative'])
def test_response_city(city):
    url = f'https://api.openbrewerydb.org/breweries?by_city={city}'
    response = requests.get(url)
    return response.text

@pytest.mark.parametrize('name', ['Almanac Beer Company', 'Curran Brewing Co', 'pussy cat dolls'], ids=['valid_value', 'valid_value', 'negative'])
def test_response_name(name):
    url = f'https://api.openbrewerydb.org/breweries?by_name={name}'
    response = requests.get(url)
    return response.text


def test_single_brewery():
    response = requests.get('https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati')
    assert response.status_code == 200


def test_query():
    response = requests.get('https://api.openbrewerydb.org/breweries/search?query=cat')
    assert response.status_code == 200


def test_by_state():
    response = requests.get('https://api.openbrewerydb.org/breweries?by_state=new_york')
    assert response.status_code == 200
