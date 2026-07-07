import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()