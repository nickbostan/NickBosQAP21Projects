import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    # iphone_11 = playwright.devices["iPhone 11 Pro"]
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }
