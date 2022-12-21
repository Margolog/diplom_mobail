import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene.support.conditions import have


class SearchResultsPage:
    button_return = (AppiumBy.CLASS_NAME, 'android.widget.ImageButton')
    search_results = (AppiumBy.CLASS_NAME, 'android.widget.TextView')

    def click_on_return(self):
        with allure.step('Нажать кнопку возврата'):
            browser.element(self.button_return).click()

    def assert_results(self):
        with allure.step('Выполнить проверку результатов поиска'):
            browser.all(self.search_results).should(have.size_greater_than(0))
