from playwright.sync_api import sync_playwright, expect, Page, Playwright
import time

def test_screenshots(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    
    #(partial)
    timestamp = str(int(time.time()))
    #page.screenshot(path=f"screenshots/homepage_{timestamp}.png")

    #(full page)
    page.screenshot(path=f"screenshots/homepage_{timestamp}.png", full_page=True)

    #(specific section)
    sec = page.locator(".product-grid.home-page-product-grid")
    sec.screenshot(path=f"screenshots/section_{timestamp}.png")