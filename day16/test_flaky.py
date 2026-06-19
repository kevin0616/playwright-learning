from playwright.sync_api import sync_playwright, expect, Page, Playwright

def test_flaky(page: Page):
    page.goto("https://demoblaze.com/index.html")
    page.locator("#login2").click()
    page.locator("#loginusername").fill("pavanol")
    page.locator("#loginpassword").fill("test@123")
    page.locator("button[onclick='logIn()']").click()

    page.wait_for_timeout(10000)

    expect(page.locator("#logout2")).to_be_visible()



'''

cmd:
pytest test_flaky.py -s -v --headed --reruns 3 --reruns-delay 2

'''