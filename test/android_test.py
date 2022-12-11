import allure
import pytest
from _pytest.fixtures import FixtureRequest
from appium.webdriver.common.appiumby import AppiumBy
from pydantic import schema
from selene import have
from selene.support.shared import browser
import utils.by
from utils import by
import conftest


def test_search_news(request: FixtureRequest):
    allure.dynamic.title(" ".join(request.node.name.split("_")[1:]).capitalize())
    with allure.step('Выполняем поиск'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Turkey")
    with allure.step('Выполняем проверку результатов поиска'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


