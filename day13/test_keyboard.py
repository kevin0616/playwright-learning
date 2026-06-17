from playwright.sync_api import sync_playwright, expect, Page


def test_keyboard(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source = page.locator("#input1")
    target1 = page.locator("#input2")    
    target2 = page.locator("#input3")


    source.focus()

    page.keyboard.insert_text("welcome")
    page.keyboard.press("Meta+A")
    page.keyboard.press("Meta+C")

    target1.focus()
    #page.keyboard.press("Tab")
    #page.keyboard.press("Tab")
    page.keyboard.press("Meta+V")

    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Meta+V")

    expect(target1).to_have_value("welcome")    
    expect(target2).to_have_value("welcome")