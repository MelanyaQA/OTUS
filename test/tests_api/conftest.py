import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default='200',
        choices=['200', '300', '400', '404', '500', '502'],
        help="This is status code"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def code(request):
    return int(request.config.getoption("--status_code"))




