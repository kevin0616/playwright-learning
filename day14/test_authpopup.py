from playwright.sync_api import sync_playwright, expect, Page, Playwright

def test_auth_popup(playwright: Playwright):
    #create a browser
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)

    #create context
    context = browser.new_context(http_credentials={"username": "admin", "password": "admin"})
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()

    expect(page.locator("text=Congratulations")).to_be_visible()

