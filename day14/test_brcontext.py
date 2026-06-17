from playwright.sync_api import sync_playwright, expect, Page, Playwright

#Browser --> context --> page/s

def test_browser_context(playwright: Playwright):
    #create a browser
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)

    #create context
    context = browser.new_context()
    #context2 = browser.new_context()
    #context3 = browser.new_context()

    page1 = context.new_page()
    page2 = context.new_page()

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(2000)
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    page2.goto("https://selenium.dev/")
    page2.wait_for_timeout(2000)
    expect(page2).to_have_title("Selenium")


