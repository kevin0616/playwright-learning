import pytest
from playwright.sync_api import Page, expect

def test_verify_css_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    '''
    #tag id
    page.locator("input#small-searchterms").fill("T-shirts")
    page.wait_for_timeout(5000)

    #tag class
    page.locator("input.search-box-text").fill("T-shirts")
    page.wait_for_timeout(5000)

    #tag attribute
    page.locator("input[name=q]").fill("T-shirts")
    page.wait_for_timeout(5000)
    '''
    #mix
    page.locator(".search-box-text[value='Search store']").fill("T-shirts")
    page.wait_for_timeout(5000)
