from playwright.async_api import async_playwright, Page, expect
import pytest

test_URL = "https://www.twitch.tv/"

@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        mypage = await browser.new_page()
        
        await mypage.goto(test_URL)
        await expect(mypage).to_have_url(test_URL)
