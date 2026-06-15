from playwright.sync_api import sync_playwright, expect, Page


def test_simple_dialogs(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #method 1
    '''
    def handle_dialog(dialog):
        dialog.accept()

    page.on("dialog", handle_dialog)
    '''

    #method 2(lambda func)
    page.on("dialog", lambda x: x.accept())

    page.locator("#alertBtn").click()

    page.wait_for_timeout(5000)


def test_confirm_dialogs(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda x: x.dismiss())

    page.locator("#confirmBtn").click()
  
    text = page.locator("#demo").inner_text()
    print(text)

def test_input_dialogs(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda x: x.accept("WonYoung"))

    page.locator("#promptBtn").click()
  
    text = page.locator("#demo").inner_text()
    print(text)
