from playwright.sync_api import sync_playwright, expect, Page

def select_date(page: Page, year, month, date, is_future):
    while 1:
        cur_month = page.locator(".ui-datepicker-month").text_content()
        cur_year = page.locator(".ui-datepicker-year").text_content()
    
        if cur_month == month and cur_year == year:
            break
        
        if is_future:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

    all_dates = page.locator(".ui-datepicker-calendar td").all()

    for d in all_dates:
        date_text = d.inner_text()
        if date_text == date:
            d.click()
            break


def test_date_picker(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date_input = page.locator("#datepicker")

    #method 1
    '''date_input.fill("10/15/2025")

    expect(date_input).to_have_value("10/15/2025")

    page.wait_for_timeout(2000)
    '''
    #method 2

    date_input.click()
    is_future = False
    select_date(page, "2020", "August", "12", is_future)

    print(date_input.input_value())
    page.wait_for_timeout(2000)