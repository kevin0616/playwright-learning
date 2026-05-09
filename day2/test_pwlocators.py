from playwright.sync_api import Page, expect
import re

test_URL = "https://demo.nopcommerce.com/"

def test_verify_pwlocators(page:Page):
   
    # 1) page.get_by_alt_text()
    '''
    page.goto(test_URL)
    page.wait_for_timeout(5000)
    logo = page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()
  
    # 2) page.get_by_text()

    expect(page.get_by_text("Welcome to our store")).to_be_visible()
    expect(page.get_by_text("Welcome to")).to_be_visible()
    expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()
    
    # 3) page.get_by_role()

    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(5000)
    expect(page.get_by_role("heading", name="Register")).to_be_visible()

    # 4) page.get_by_label()
    
    page.get_by_label("First name:").fill("KK")
    page.get_by_label("Last name:").fill("Yen")
    page.get_by_label("Email:").fill("abc@gmail.com")
    
    page.wait_for_timeout(2000)

    # 5) page.get_by_placeholder()
    
    page.goto(test_URL)
    page.get_by_placeholder("Search store").fill("hello")
    
    page.wait_for_timeout(2000)
    '''

    # 6) page.get_by_title
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")    
    expect(page.get_by_title("Hypertext Markup Language")).to_have_text("HTML")
    #page.wait_for_timeout(2000)

    # 7) page.get_by_test_id

    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")

    page.wait_for_timeout(3000)