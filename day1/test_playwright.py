from playwright.sync_api import Page, expect

test_URL = "https://www.twitch.tv/"

def test_verifyPageUrl(page:Page):
    page.goto(test_URL)

    print("Page URL is", page.url)

    expect(page).to_have_url(test_URL)

def test_verifyTitle(page:Page):
    page.goto(test_URL)

    print("Page title is", page.title())

    expect(page).to_have_title("Twitch")

