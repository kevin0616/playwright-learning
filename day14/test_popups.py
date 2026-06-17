from playwright.sync_api import sync_playwright, expect, Page, Playwright

def test_browser_context(playwright: Playwright):
    #create a browser
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)

    #create context
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")
    
    page.on("popup", lambda x: x.wait_for_load_state())

    page.locator("#PopUp").click()
    page.wait_for_timeout(2000)
    print("Total number of popups:", len(context.pages))

    print("Content:", context.pages)

    for p in context.pages:
        print(p.url)
        if "Playwright" in p.title():
            p.locator(".getStarted_Sjon").click()
            p.wait_for_timeout(2000)
            expect(p).to_have_title("Installation | Playwright")

