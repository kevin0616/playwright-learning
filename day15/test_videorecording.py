from playwright.sync_api import sync_playwright, expect, Page, Playwright

def test_record_video(playwright: Playwright):
    #create a browser
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)

    #create context
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1024, "height": 768}
    )

    page = context.new_page()

    page.goto("https://demoblaze.com/index.html")
    page.locator("#login2").click()
    page.locator("#loginusername").fill("pavanol")
    page.locator("#loginpassword").fill("test@123")
    page.locator("button[onclick='logIn()']").click()

    page.wait_for_timeout(1000)