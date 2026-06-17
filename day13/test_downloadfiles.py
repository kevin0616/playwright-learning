from playwright.sync_api import sync_playwright, expect, Page


def test_download_files(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("test download")

    page.locator("#generateTxt").click()

    def handle_download(download):
        download.save_as("../downloads/testfile.txt")

    #page.on("download", handle_download)
    page.on("download", lambda x: x.save_as("../downloads/testfile.txt"))
    
    page.locator("#txtDownloadLink").click()

    page.wait_for_timeout(3000)