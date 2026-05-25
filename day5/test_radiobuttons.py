import pytest
from playwright.sync_api import Page, expect

def test_tradio_buttons(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    radio = page.locator("#male")    

    expect(radio).to_be_visible()
    expect(radio).to_be_enabled()

    expect(radio).not_to_be_checked()
    
    radio.check()
    expect(radio).to_be_checked()
    

