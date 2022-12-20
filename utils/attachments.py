import allure
from allure_commons.types import AttachmentType


def add_video(browser):
    video_url = "https://app-automate.browserstack.com/s3-upload/bs-video-logs-euw/s3.eu-west-1/" \
                f"{browser.driver.session_id}/video-{browser.driver.session_id}.mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def add_screenshot(browser):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


def add_xml_dump(browser):
    allure.attach(
        browser.driver.page_source,
        name='page xml dump',
        attachment_type=allure.attachment_type.XML
    )
