import pytest
from playwright.sync_api import sync_playwright, expect, Page

search_items = ["laptop", "Gift card", "smartphone", "monitor"]

@pytest.mark.parametrize("item", search_items)
def test_search_items(item, page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(item)
    page.locator("input[value='Search']").click()

    result = page.locator("h2 a").nth(0)
    expect(result).to_contain_text(item, ignore_case=True)