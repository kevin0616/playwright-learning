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

    print("First computer product:", products.first.text_content())
    print("Last computer product:", products.last.text_content())
    print("Nth computer product:", products.nth(2).text_content())

    product_titles = products.all_text_contents()
    print("Product titles:", product_titles)

    #xpath with start-with
    building_products = page.locator("//h2//a[starts-with(@href,'/build')]")    
    print("Count of building products:", building_products.count())

    #xpath with text() --- it's innertext
    registration_link = page.locator("//a[text()='Register']")
    expect(registration_link).to_be_visible()

    google_plus_link = page.locator("//div[@class='column follow-us']//li[last()]")
    expect(google_plus_link).to_have_text("Google+")

    #xpath with postion()
    twitter_link = page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitter_link).to_have_text("Twitter")

    