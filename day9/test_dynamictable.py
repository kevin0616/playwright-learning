from playwright.sync_api import sync_playwright, expect, Page

def test_dynamic_table(page: Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    table = page.locator("table.table tbody")
    expect(table).to_be_visible()

    #1. count # of rows in table
    rows = table.locator("tr").all()

    for r in rows:
        name = r.locator("td").nth(0).inner_text()
        #print(name)
        if name == "Chrome":
            cpu_load = r.locator("td:has-text('%')").inner_text()
            print("CPU load of Chrome:", cpu_load)
            break

    expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)

    page.wait_for_timeout(2000)