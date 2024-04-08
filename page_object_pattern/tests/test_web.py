import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from pages.web import TreesPage
from selenium.webdriver import Chrome


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
def test_basic_duckduckgo_search(browser):
    # Настройте данные для тест-кейса
    PHRASE = 'cars'

    # Поиск фразы
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    # Проверка, что результаты появились
    result_page = DuckDuckGoResultPage(browser)

    assert result_page.search_results_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE
    
def test_geo_in_wiki(browser):
    # Настройте данные для тест-кейса
    PHRASE = 'Eiffel Tower'

    # Поиск фразы
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    # Проверка, что результаты появились
    result_page = DuckDuckGoResultPage(browser)

    assert result_page.search_results_count() > 0
    assert result_page.search_geo_in_wiki() > 0

def test_web(browser):
    trees_page = TreesPage(browser)
    trees_page.load()
    trees_page.find_variant()
    # Реализация проверок с помощью PyTest
    assert trees_page.supernatural_elements_count() > 5
    assert trees_page.dean_elements_count() > 0
    assert trees_page.john_winchester_elements_count() > 0
    assert trees_page.sam_winchester_elements_count() > 0
    assert trees_page.heading_images_count() > 0
    assert trees_page.title_elements_count() > 0
    assert trees_page.images_loaded_count() > 5