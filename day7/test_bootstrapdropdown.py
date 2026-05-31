import pytest
from playwright.sync_api import Page, expect

def test_bootstrap_dropdown(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #login steps
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()


    page.get_by_text("PIM").click()

    page.locator("form i").nth(2).click()
    page.wait_for_timeout(2000)

    options = page.locator("div[role='listbox'] span")

    count = options.count()
    print("Number of options:", count)

    expect(options).to_have_count(count)

    page.wait_for_timeout(2000)
    

    #print("All options from the dropdown", options.all_text_contents())


    for i in range(count):
        print(options.nth(i).text_content())

    for i in range(count):
        if options.nth(i).text_content() == "Account Assistant":
            options.nth(i).click()
            break
    
    page.wait_for_timeout(2000)