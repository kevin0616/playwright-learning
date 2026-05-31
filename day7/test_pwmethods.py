import pytest
from playwright.sync_api import Page, expect

def test_comparisonofmethods(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    products = page.locator(".product-title")

    #print("Using innter_text():", products.nth(1).inner_text())    
    #print("Using text_content():", products.nth(1).text_content())

    for i in range(products.count()):
        print(products.nth(i).inner_text())    
    
    for i in range(products.count()):    
        print(products.nth(i).text_content().strip())

    products_locator = products.all()

    print("HI", products_locator[0].inner_text())

    '''
    1. inner_text() vs text_content()
    2. all_inner_texts() vs all_text_contents()
    3. all()

    inner_text is processed and text_content you have to do the trim / strip
    
    '''