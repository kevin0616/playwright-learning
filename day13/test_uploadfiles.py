from playwright.sync_api import sync_playwright, expect, Page


def test_upload_files(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#singleFileInput").set_input_files("../uploads/file1.txt")

    submit = page.locator("button:has-text('Upload Single File')")
    submit.click()

    page.wait_for_timeout(2000)

    info = page.locator("#singleFileStatus").inner_text()
    print(f"Upload Status: {info}")

def test_multiple_files(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#multipleFilesInput").set_input_files(["../uploads/file1.txt"])

    submit = page.locator("button:has-text('Upload Multiple Files')")
    submit.click()

    page.wait_for_timeout(2000)

    info = page.locator("#multipleFilesStatus").inner_text()
    print(f"Upload Status: {info}")


