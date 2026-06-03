from playwright.sync_api import sync_playwright, expect, Page
   
'''def test_pagination_table(page: Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    more_pages = True

    while more_pages:
        rows = page.locator("#example tbody tr").all()
        
        for r in rows:
            print(r.inner_text())
        page.wait_for_timeout(2000)

        next_button = page.locator("button[aria-label='Next']")
        is_disabled = next_button.get_attribute("class")
        
        if "disabled" in is_disabled:
            more_pages = False
        else:
            next_button.click()
'''
    

def test_booking_page(page: Page):
    page.goto("https://blazedemo.com/")

    #1. select flight
    depart = page.locator("select[name='fromPort']")
    dest = page.locator("select[name='toPort']")

    depart.select_option("Boston")
    dest.select_option("New York")

    submit = page.locator("input")
    expect(submit).to_be_enabled()
    submit.click()

    #page.wait_for_timeout(3000)
    #2. select cheapest flight
    table = page.locator("table tbody")
    rows = table.locator("tr")
    rows_data = rows.all()

    headers = table.locator("th")
    headers_count = headers.count()
 
    min_price = float("inf")
    flight = -1
    index = -1
    for i, r in enumerate(rows_data):

        price = r.locator("td").nth(5).inner_text()
        price = float(price[1:])
        if price < min_price:
            min_price = price
            flight = r.locator("td").nth(1).inner_text()
            index = i

    print(f"Cheapest flight: #{flight}, price: ${min_price}")

    rows_data[index].locator("td").nth(0).locator("input").click()


    #page.wait_for_timeout(2000)
    #3. fill in user data
    page.locator("#inputName").fill("Kevin Y")
    page.locator("#address").fill("946 Bedford Ave")
    page.locator("#city").fill("Brooklyn")
    page.locator("#state").fill("NY")
    page.locator("#zipCode").fill("11205")
    page.locator("#cardType").select_option("Visa")
    page.locator("#creditCardNumber").fill("1234777712347777")
    page.locator("#creditCardMonth").fill("10")
    page.locator("#creditCardYear").fill("2029")
    page.locator("#nameOnCard").fill("KKK")
    page.locator("#rememberMe").check()
    page.locator("input[type='submit']").click()


    page.locator("input[type='submit']").click()

    page.wait_for_timeout(2000)


