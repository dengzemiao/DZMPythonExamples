# 手动设置 Chromium 浏览器的路径
chromium_path = "./venv/lib/python3.11/site-packages/playwright/driver/package/.local-browsers/chromium-1134/chrome-mac/Chromium.app/Contents/MacOS/Chromium"

import asyncio
from playwright.async_api import async_playwright

async def run_task_in_new_window(browser, url, screenshot_name):
    # 打开一个新页面 (窗口)
    page = await browser.new_page()
    # 访问网址
    await page.goto(url)
    # 等待 5 秒
    await asyncio.sleep(10000000)
    # 截图并保存
    # await page.screenshot(path=screenshot_name)
    # 关闭页面
    # await page.close()

async def main():
    async with async_playwright() as p:
        # 启动浏览器
        browser = await p.chromium.launch(executable_path=chromium_path, headless=False)
        
        # 并发执行多个任务
        await asyncio.gather(
            run_task_in_new_window(browser, "https://example.com", "example1.png"),
            run_task_in_new_window(browser, "https://playwright.dev", "example2.png"),
            run_task_in_new_window(browser, "https://github.com", "example3.png")
        )
        
        # 关闭浏览器
        # await browser.close()

asyncio.run(main())

