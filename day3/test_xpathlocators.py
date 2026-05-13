import pytest
from playwright.sync_api import Page, expect

def test_verify_xpath_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    # absolute xpath
    logo = page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()

    #reletive xpath (starts with //)
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(5000)

    #contains()
    products = page.locator("//h2//a[contains(@href,'computer')]")
    products_count = products.count()

    print("Products count:", products_count)

    expect(products).to_have_count(products_count)

    print(products.first.text_content())
    print(products.last.text_content())
    print(products.nth(2).text_content())