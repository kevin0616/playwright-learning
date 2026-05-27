import pytest
from playwright.sync_api import Page, expect

def test_sorted_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    

    #dropdown_options = page.locator("#colors>option")
    dropdown_options = page.locator("#animals>option")
    
    options_text = [text.strip() for text in dropdown_options.all_text_contents()]
    original_list = options_text.copy()
    sorted_list = sorted(options_text)

    print("Original list:", original_list)
    print("Sorted list:", sorted_list)

    if original_list == sorted_list:
        print("It's sorted")
    else:
        print("It's not sorted")

    page.wait_for_timeout(2000)
    

