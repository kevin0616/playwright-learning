import pytest
from playwright.sync_api import Page, expect

def test_inputbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    text_box = page.locator("#name")
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()
    
    expect(text_box).to_have_attribute("maxlength", "15")
    print(text_box.get_attribute("maxlength"))

    text_box.fill("Kevin")
    print("Entered value:", text_box.input_value())

    page.wait_for_timeout(2000)
    
