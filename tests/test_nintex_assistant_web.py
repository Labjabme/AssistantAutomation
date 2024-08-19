import re
import allure
import pytest

from playwright.sync_api import Page, expect, sync_playwright


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True

    }


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()


#     page.goto("https://static.nintextest.io/assistant/v2024.1.1000000017/index.html")
#
#
# # With following 3 lines we are expecting a new page to be open.
# # Once the event of new page is fired, we catch that page and we save in new_page_info.
# with context.expect_page() as new_page_info:
#     page.wait_for_timeout(5000)
#     page.click("//span[text()='Cookie Policy']")  # Opens a new tab
# # Once we have the event of new page, we get the attribute "value", which is the actual page
# new_page = new_page_info.value
# new_page.wait_for_timeout(5000)


def test_has_title(page: Page):
    page.goto("https://static.nintextest.io/assistant/v2024.1.1000000017/index.html")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Nintex Assistant"))


@pytest.mark.suite_id("112233")
@pytest.mark.test_case("445556")
@allure.title("Test Nintex Assistant_Web assert")
@pytest.mark.functional
def test_nintex_assistant(page: Page):
    page.goto("https://static.nintextest.io/assistant/v2024.1.1000000017/index.html")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


@allure.title("Test Nintex Assistant_Web")
@pytest.mark.functional
def test_nintex_assistant_ui(page: Page) -> None:
    page.goto("https://static.nintextest.io/assistant/v2024.1.1000000016/index.html")
    expect(page.get_by_text("Nintex Assistant Meet our AI")).to_be_visible()


def test_nintex_assistant_ui_q_and_a(page: Page) -> None:
    page.goto("https://static.nintextest.io/assistant/v2024.1.1000000017/index.html?product=docgen")
    expect(page.get_by_label("Generative AI is experimental")).to_contain_text("Generative AI is experimental")
    page.get_by_text("Welcome to DocGen Help. What").click()
    page.get_by_text("Welcome to DocGen Help. What").click()
    expect(page.locator("#root")).to_contain_text("Welcome to DocGen Help. What are you trying to solve today?")
    expect(page.locator("#root")).to_contain_text(
        "How can a DocGen admin manage user permission sets and DocGen licenses for production and sandbox "
        "environments?")
    page.get_by_text("How can a DocGen admin manage").click()
    page.get_by_text("Generating...").click()
    page.get_by_text("Generating...").click()
    expect(page.locator("#root")).to_contain_text(
        "Error while processing question: TypeError: Cannot read properties of undefined (reading 'data')")
    expect(page.locator("#root")).to_contain_text("Welcome to DocGen Help. What are you trying to solve today?")
    page.locator("div").filter(
        has_text=re.compile(r"^Welcome to DocGen Help\. What are you trying to solve today\?$")).nth(1).click()
