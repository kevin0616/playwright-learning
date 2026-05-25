import pytest
from playwright.sync_api import Page, expect

def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#country")

