import pytest
import requests


def test_url_status(base_url, code):
    target = base_url + f"/status/{code}"
    response = requests.get(url=target)
    assert response.status_code == code


