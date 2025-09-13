from selene import browser, have


def test_search_for_google(open_browser):
    search_box = browser.element('[id*="input"]')
    search_box.clear()
    search_box.type('google').press_enter()
    browser.element('html').should(have.text('google'))

def test_search_random_gibberish_no_results(open_browser, chaos_query):
    search_box = browser.element('[id*="input"]')
    search_box.clear()
    search_box.type(chaos_query).press_enter()
    browser.element('body').should(have.text(f'No results found'))
