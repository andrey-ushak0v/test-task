import os
import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    driver = item.funcargs.get("browser")  
    report = outcome.get_result()
    if report.when == 'call' and report.outcome == "failed":
        screenshot_path = f"screenshots/{item.name}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(screenshot_path)
