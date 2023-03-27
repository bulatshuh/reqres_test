import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://reqres.in/',
                     help="Enter url to send request")

    parser.addoption('--browser', action='store', default='chrome',
                     help="Enter wanted browser - chrome")


@pytest.fixture(scope='session')
def get_base_url(request):
    user_url = request.config.getoption('url')
    yield user_url


@pytest.fixture(scope='class')
def get_browser(request):
    browser_name = request.config.getoption('browser')
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
        print('\nOpening Chrome...')
    # можно добавить другие браузеры
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')
    yield browser
    print('\nClosing browser...')
    browser.quit()
