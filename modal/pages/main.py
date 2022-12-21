import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene.support.conditions import be


class MainPage:
    field_search_init = (AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')
    field_search_do = (AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')
    button_action_menu = (AppiumBy.ID, 'org.wikipedia.alpha:id/menu_overflow_button')
    button_settings = (AppiumBy.ID, 'org.wikipedia.alpha:id/explore_overflow_settings')
    title = (AppiumBy.ID, 'org.wikipedia.alpha:id/single_fragment_toolbar_wordmark')

    def search_item(self, value):
        with allure.step('Поиск'):
            browser.element(self.field_search_init).click()
            browser.element(self.field_search_do).type(value)


    def assert_main(self):
        with allure.step('Проверка заголовка на главной странице'):
            browser.element(self.title).should(be.visible)