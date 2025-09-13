import random
import time

import pytest
from selene import browser


@pytest.fixture(scope='session')
def open_browser():
    print('opening browser')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://duckduckgo.com/')

    yield browser

    browser.quit()

@pytest.fixture
def chaos_query():
    timestamp = str(int(time.time()))
    random_letters = ''.join(random.choices('ващшоывнцуъъхх', k=8))
    query = f"zzxqweasd{timestamp}{random_letters}notfound"
    return query