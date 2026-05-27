import pytest
from playwright.sync_api import Page, expect

def test_multiple_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #by label
    page.locator("#colors").select_option(["Blue", "Yellow", "White"])
    page.locator("#colors").select_option(label=["Blue", "Yellow", "White"])
    page.wait_for_timeout(2000)

    #by value
    page.locator("#colors").select_option(value=["red", "green"])
    page.wait_for_timeout(2000)

    #by index
    page.locator("#colors").select_option(index=[0, 1, 2])
    page.wait_for_timeout(2000)


    dropdown_options = page.locator("#colors>option")
    expect(dropdown_options).to_have_count(7)

    options_text = [text.strip() for text in dropdown_options.all_text_contents()]

    print(options_text)

    

