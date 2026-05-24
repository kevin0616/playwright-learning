import pytest
from playwright.sync_api import Page, expect
import re

'''
css: 
name^='st' equals to start with in xpath
name*='st' equals to contains in xpath
'''


def test_handle_dynamic_elements(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    for i in range(5):
        button = page.locator("//button[text()='STOP' or text()='START']")
        #button = page.locator("button[name^='st']")
        button.click()
        page.wait_for_timeout(2000)

def test_handle_dynamic_elements_css(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    for i in range(5):
        #button = page.locator("//button[text()='START' or text()='STOP]")
        button = page.locator("button[name^='st']")
        button.click()
        page.wait_for_timeout(2000)

def test_handle_dynamic_elements_playwright(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    for i in range(5):
        button = page.get_by_role('button', name=re.compile('ST.*'))
        button.click()
        page.wait_for_timeout(2000)
