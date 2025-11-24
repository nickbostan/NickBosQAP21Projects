import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://playwright.dev/")
    yield
    print("afterEach")


def test_has_title(page: Page):
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
