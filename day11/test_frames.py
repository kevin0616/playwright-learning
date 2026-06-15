from playwright.sync_api import sync_playwright, expect, Page


def test_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frame = page.frames

   

    print(f"Number of frames: {len(frame)}")

    #method1
    frame1 = page.frame(url="url of the frame")
    #method2
    frame1 = page.frame("name of the frame")

    frame1.locator("input").fill("Welcome")
    
    page.wait_for_timeout(2000)