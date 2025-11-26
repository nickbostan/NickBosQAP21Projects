import re
import time

import pytest
from playwright.sync_api import Page, expect

from files import FILES, IMG_1


@pytest.mark.browser_context_args(timezone_id="Europe/Berlin", locale="de-DE")
def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))


def test_bing_is_working(page):
    page.goto("https://bing.com")


@pytest.mark.only
def test_set_files(page: Page):
    page.goto("https://practice-automation.com/file-upload/")

    page.locator('[type="file"]').set_input_files(IMG_1)
    page.locator("id=upload-btn").click()

    expect_loc = page.get_by_role("status")

    expect(expect_loc).to_contain_text("Thank you for your message. It has been sent.")


@pytest.mark.only
def test_download_file(page: Page):
    page.goto("https://practice-automation.com/file-download/")
    page.locator(".wpdm-download-link.download-on-click").highlight()
    with page.expect_download() as download_info:
        page.locator(".wpdm-download-link.download-on-click").nth(0).click()

    download_file = download_info.value
    download_file.save_as(FILES / download_file.suggested_filename)


def test_codegen(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").press_sequentially(
        "купить хлеб "
    )
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill(
        "поздравить маму с празником"
    )
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("сходить к врачу ")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("listitem").filter(has_text="купить хлеб").get_by_label(
        "Toggle Todo"
    ).check()
    page.get_by_role("listitem").filter(
        has_text="поздравить маму с празником"
    ).get_by_label("Toggle Todo").check()
    page.get_by_role("listitem").filter(has_text="сходить к врачу").get_by_label(
        "Toggle Todo"
    ).check()
    page.get_by_role("link", name="Completed").click(force=True)
    page.get_by_text("купить хлеб").click()
    page.get_by_text("поздравить маму с празником").click()
    page.get_by_text("сходить к врачу").click()
    page.get_by_text("0 items leftAll Active").click()
    page.get_by_role("link", name="Active").click()
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_text("All Active Completed").click()
    expect(page.get_by_role("textbox", name="What needs to be done?")).to_be_visible()
    page.get_by_text("All Active Completed").click()
    expect(page.locator("body")).to_contain_text("Completed")

    page.locator("body").highlight()
    time.sleep(20)

    page.get_by_role("link", name="All").click()
    page.get_by_text("поздравить маму с празником").click()
    expect(page.locator("body")).to_contain_text("сходить к врачу")


@pytest.mark.only
def test_page_form(page: Page):
    page.goto("https://practice-automation.com/form-fields/")
    expect(page).to_have_title(re.compile("Form Fields"))
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").press_sequentially("NICKboss")
    page.get_by_role("textbox", name="Password").focus()
    page.get_by_role("textbox", name="Password").fill("Password123")
    expect(page.get_by_text("NICKboss")).to_be_visible()
    expect(page.get_by_text("fjfj@gmail.com")).to_be_visible()
    page.get_by_text("Wine").click()
    page.get_by_test_id("color1").click()
    page.get_by_test_id("automation").click()
    page.get_by_test_id("message").click()
    expect(page.get_by_text("Wine")).to_be_visible()
    expect(page.get_by_test_id("color1")).to_be_checked()
    expect(page.get_by_test_id("automation")).to_be_checked()
    page.get_by_test_id("submit-btn").click()
