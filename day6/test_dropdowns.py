import pytest
from playwright.sync_api import Page, expect

def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #by label
    page.locator("#country").select_option("Japan")
    page.locator("#country").select_option(label="Japan")
    page.wait_for_timeout(2000)

    #by value
    page.locator("#country").select_option("germany")
    page.locator("#country").select_option(value="germany")
    page.wait_for_timeout(2000)

    #by index
    page.locator("#country").select_option(index=3)
    page.wait_for_timeout(2000)


    dropdown_options = page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)

    options_text = [text.strip() for text in dropdown_options.all_text_contents()]

    print(options_text)

    

