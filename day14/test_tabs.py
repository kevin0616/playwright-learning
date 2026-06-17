from playwright.sync_api import sync_playwright, expect, Page, Playwright

def test_tabs(playwright: Playwright):
    #create a browser
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)

    #create context
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")
    
    page.on("page", lambda x: x.wait_for_load_state())

    page.locator("button[onclick='myFunction()']").click()
    page.wait_for_timeout(2000)

    all_pages = context.pages

    print("Number of pages:", len(all_pages))
    
    print("Title of parent page:", all_pages[0].title())    
    print("Title of child page:", all_pages[1].title())    
 
    print("URL of parent page:", all_pages[0].url)    
    print("URL of child page:", all_pages[1].url)    


'''
types of events
alerts/dialog: "dialog"
download files: "download"
popups: "popup"
tabs: "page"

page.on()

'''