from playwright.sync_api import sync_playwright, expect, Page, Playwright

def test_trace(playwright: Playwright):
    #create a browser
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)

    #create context
    context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()

    page.goto("https://demoblaze.com/index.html")
    page.locator("#login2").click()
    page.locator("#loginusername").fill("pavanol")
    page.locator("#loginpassword").fill("test@123")
    page.locator("button[onclick='logIn()']").click()

    page.wait_for_timeout(1000)

    context.tracing.stop(path="trace.zip")

    context.close()
    browser.close()


'''
command to show tracefile:
playwright show-trace trace.zip
or 
put zip file to website
'''