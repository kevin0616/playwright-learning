import pytest
from playwright.sync_api import sync_playwright, expect, Page
'''
different method of reading(json, csv, excelfile)
'''
import json
import csv
#pip install openpyxl

login_data = [("laura.taylor1234@example.com", "test123", "valid"),
              ("invaliduser@example.com", "test321", "invalid"),
              ("validuser@example.com", "testxyz", "invalid"),
              ("", "", "invalid"),]

@pytest.mark.parametrize("email, password, validity", login_data)
def test_search_items(email, password, validity, page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator(".ico-login").click()
    page.wait_for_load_state()
    page.locator("#Email").fill(email)
    page.locator("#Password").fill(password)
    page.locator("input[value='Log in']").click()

    if validity == "valid":
        expect(page.locator(".ico-logout")).to_be_visible()

    else:
        expect(page.locator("div[class='validation-summary-errors'] span")).to_contain_text("Login was unsuccessful. Please correct the errors and try again.")

