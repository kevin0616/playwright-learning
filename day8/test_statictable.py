from playwright.sync_api import sync_playwright, expect, Page

def test_static_table(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    #1. count # of rows in table
    rows = table.locator("tr")
    expect(rows).to_have_count(7)

    rows_count = rows.count()
    print("Number of rows:", rows_count)

    #2. count # of columns in table
    headers = rows.locator("th")
    expect(headers).to_have_count(4)

    headers_count = headers.count()
    print("Number of headers:", headers_count)

    second_row_cells = rows.nth(2).locator("td")
    #print(second_row_cells.all_inner_texts())


    for i in range(1, rows_count):
        print(rows.nth(i).locator("td").all_inner_texts())

    all_row_data = rows.all()

    #for r in all_row_data[1:]:
    #    print(r.locator("td").all_inner_texts())

    #conditional print
    for r in all_row_data[1:]:
        author_name = r.locator("td").nth(1).inner_text()
        if author_name == "Mukesh":
            print("Bookname:", r.locator("td").nth(0).inner_text())
        
    #total price
    total_price = 0
    for r in all_row_data[1:]:
        total_price += int(r.locator("td").nth(3).inner_text())

    print("Total price:", total_price)