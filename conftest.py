import os
import pytest
from appium import webdriver
from dotenv import load_dotenv
from utils.attachments import *
from selene.support.shared import browser
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    load_dotenv()
    username = os.getenv('USER_NAME')
    accesskey = os.getenv('ACCESS_KEY')
    app = os.getenv('APP')

    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": f'{app}',
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": f'{username}',
            "accessKey": f'{accesskey}'
        }
    })

    browser.config.driver = webdriver.Remote(
        command_executor="http://hub.browserstack.com/wd/hub",
        options=options,
    )

    browser.config.timeout = 4
    yield setup_browser

    add_video(browser)
    add_screenshot(browser)
    add_xml_dump(browser)
    browser.quit()