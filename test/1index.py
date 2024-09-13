# 导入
from playwright.sync_api import Playwright, sync_playwright

# 创建浏览器
def run (playwright: Playwright) -> None:

  # 创建浏览器
  browser = playwright.chromium.launch(headless=False)

  # 新建窗口
  content = browser.new_context()

  # 新建页面
  page = content.new_page()

  # 访问首页
  page.goto('file:///Users/dengzemiao/Desktop/GitHub/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B6%E5%A4%B9/DZMLuckyDrawPro/index.html')

  # 延迟
  page.wait_for_timeout(1000)

  # page.hover('//a[@class="ant-dropdown-link ant-dropdown-trigger"]')
  # page.click('//a[@class="ant-dropdown-link ant-dropdown-trigger"]')
# ant-dropdown-trigger

  # el = page.locator('.ant-dropdown-trigger1')
  el = page.query_selector('.ant-dropdown-trigger')
  print(el)

  # el.hover()
  # # 点击登录
  # page.click('//a[@href="/login"]')

  # # 延迟
  # page.wait_for_timeout(1000)

  # # 密码登录
  # page.click('//a[contains(text(), "密码登录")]')

  # # 写入账号
  # page.fill('//input[@id="LAY-user-login-branchCode"]', 'wh1')
  # page.fill('//input[@id="LAY-user-login-username"]', '10086')

  # # # 写入密码
  # page.fill('//input[@id="LAY-user-login-password"]', '123456')

  # # 延迟
  # page.wait_for_timeout(1000)

  # # 点击登录
  # page.click('//button[@id="loginBtn"]')

  # # 延迟
  # page.wait_for_timeout(1000)

  # # 点击仓储业务
  # page.click('//a[@id="wms"]')

  # # 延迟
  # page.wait_for_timeout(1000)

  # # 点击库存管理
  # page.click("//cite[contains(text(), '库存管理')]")

  # # 延迟
  # page.wait_for_timeout(1000)

  # # 点击库存记录
  # page.click("//a[contains(text(), '库存记录')]")

  # # 延迟
  # page.wait_for_timeout(1000)

  # # 点击库存记录
  # page.click("//a[contains(text(), '库存记录')]")

  # # 延迟
  # page.wait_for_timeout(5000)

  # print(1111)


  # # 点击库存记录
  # page.click("//span[contains(text(), '更多')]")

  # dropdown = page.locator('.ant-dropdown-trigger')

  # print(dropdown)

  # dropdown.hover()

  # page.hover("//span[contains(text(), '更多')]")

  # ant-dropdown-hidden


  # hover 出菜单（失败）
  # page.hover('//div[@class="nav-adv nav-adv-home u-info"]/p')
  # page.wait_for_selector('//div[@class="nav-adv nav-adv-home u-info"]/ul', state='visible', timeout=30000)
  # page.locator('//div[@class="nav-adv nav-adv-home u-info"]/ul')
  # 延迟
  # page.wait_for_timeout(1000)
  # 点击财务管理
  # page.click('//a[@href="/pipeline-record"]')

  # # 上面 hover 失败，那就直接手动加载网页
  # page.goto('https://hepai.video/pipeline-record')

  # # 延迟
  # page.wait_for_timeout(1000)

  # # hover 出菜单
  # page.hover('//div[@class="u-info"]/img')

  # # 退出登录
  # page.click('//a[contains(text(), "退出登录")]')

  # # 点击确定按钮
  # page.click('//button/span[contains(text(), "确")]/..')

  # # 延迟
  page.wait_for_timeout(20000)

  # 关闭上下文
  content.close()

  # 关闭浏览器
  browser.close()

# 调用
with sync_playwright() as playwright:
  run(playwright)
