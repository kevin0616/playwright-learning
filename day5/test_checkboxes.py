import pytest
from playwright.sync_api import Page, expect

def test_check_boxes(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    check_box_sunday = page.locator("#sunday")    

    expect(check_box_sunday).to_be_visible()
    expect(check_box_sunday).to_be_enabled()

    expect(check_box_sunday).not_to_be_checked()
    
    check_box_sunday.check()
    expect(check_box_sunday).to_be_checked()

    page.wait_for_timeout(2000)
    


    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    checkboxes = []

    for d in days:
        checkbox = page.get_by_label(d)
        checkboxes.append(checkbox)

    print("Number of checkboxes:", len(checkboxes))

    for c in checkboxes:
        c.check()
        expect(c).to_be_checked()
    
    page.wait_for_timeout(2000)

    for c in checkboxes:
        if c.is_checked():
            c.uncheck()
        else:
            c.check()

    page.wait_for_timeout(2000)
