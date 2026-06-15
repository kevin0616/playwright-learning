from playwright.sync_api import sync_playwright, expect, Page


def test_mouse_hover(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    target = page.locator(".dropbtn")

    target.hover()

    laptops = page.locator(".dropdown-content a:nth-child(2)")
    laptops.hover()

    page.wait_for_timeout(1000)

def test_mouse_rightclick(page: Page):
    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")

    target = page.locator(".context-menu-one")

    target.click(button='right')

    page.wait_for_timeout(1000)

def test_mouse_doubleclick(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    target = page.locator("button[ondblclick='myFunction1()']")

    target.dblclick()

    context = page.locator("#field1").input_value()
    print(f"Copied contexts: {context}")

    page.wait_for_timeout(1000)

def test_mouse_drag_drop(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source = page.locator("#draggable")
    target = page.locator("#droppable")

    #approach 1
    source.hover()
    page.mouse.down()
    target.hover()
    page.mouse.up()

    #approach 2
    source.drag_to(target)

    page.wait_for_timeout(2000)
