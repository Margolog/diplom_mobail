import allure
from modal import app


@allure.title('Test search item')
def test_search_item():
    app.main_page.search_item('Turkey')
    app.search_results_page.assert_results()


@allure.title('Test search symbols')
def test_search_symbols():
    app.main_page.search_item('###')
    app.search_results_page.assert_results()


@allure.title('Test search space')
def test_search_space():
    app.main_page.search_item('  ')
    app.search_results_page.assert_results()


@allure.title('Test search numbers')
def test_search_numbers():
    app.main_page.search_item('11111')
    app.search_results_page.assert_results()


@allure.title('Test return to main')
def test_return_to_main():
    app.main_page.search_item('Turkey')
    app.search_results_page.click_on_return()
    app.main_page.assert_main()


