from playwright.sync_api import sync_playwright

def scrape_chapter(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        screenshot_path = "chapter_screenshot.png"
        page.screenshot(path=screenshot_path)
        browser.close()
        return content, screenshot_path
