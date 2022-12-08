import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser



def test_search_news():
    with allure.step('Выполняем поиск'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Turkey")
    with allure.step('Выполняем проверку результатов поиска'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


