# encoding:utf-8
# 浏览器
from playwright.sync_api import Playwright, sync_playwright
# 外部传参
import argparse
# json 处理
import json
# 系统库
import sys
import os

# 结束脚本


def done():
    # 输出日志
    output_log()
    # 退出脚本
    sys.exit()
# 退出登录


def logout(browser, content, page):
    # 点击退出按钮
    page.click('//button[@id="btn-logout"]')
    # 延迟
    page.wait_for_timeout(2000)
    # 关闭上下文
    content.close()
    # 关闭浏览器
    browser.close()
# 输出日志


def output_log():
    # 同步数据到文件
    with open(path_log, 'w', encoding='utf-8') as f:
        # 组装内容
        msg = '总金额（转出成功）：%f\n' % config['amount']
        for item in config['list']:
            msg += '账户：%s 转出：%f 结果：%s\n' % (item['account'],
                                            item['balance'], item['msg'])
        # 把新内容写回硬盘
        f.write(msg)


# 配置文件路径
path = os.path.dirname(os.path.realpath(sys.executable))
path_account = path + '/account.txt'
path_log = path + '/log.txt'
path_account = './account.txt'
path_log = './log.txt'
# 定义命令行解析器对象
parser = argparse.ArgumentParser(description='脚本参数介绍')
# 添加命令行参数（--xxx 为固定写法）
parser.add_argument('--path', type=str, default=path_account,
                    help='导入账号 json 列表文件，例如 xxx.json，默认路径：%s' % path_account)
parser.add_argument('--headless', type=int, default=0,
                    help='是否使用无界面浏览器： 0 有界面 1 无界面，默认：0')
# 从命令行中结构化解析参数
args = parser.parse_args()
# 配置对象
config = {
    'account': '',  # 主账户
    'amount': 0,  # 转账成功的总金额
    'list': [  # 子账户列表
        # {
        #   'account': '', # 账号
        #   'password': '', # 密码
        #   'balance': 0, # 余额
        #   'msg': '等待' # 结果
        # }
    ]
}
try:
    # 获取账户列表
    with open(args.path, 'r', encoding="utf-8") as f:
        # 读取字符串
        str = f.read()
        # 分割账号
        strs = str.split('\n')
        # 配置对象
        for item in strs:
            # 分割账号
            list = item.split('-')
            # 判断是否为主账户
            if 'root' in list[1]:
                # 主账户
                config['account'] = list[0]
            else:
                # 生成子账户
                account = {
                    'account': list[0],
                    'password': list[1],
                    'balance': 0,
                    'msg': '等待'
                }
                # 加入子账户列表
                config['list'].append(account)
except:
    print(
        '\033[1;31m=========================== logs =========================== \033[0m')
    print('检查配置文件路径否有效')
    print(
        '\033[1;31m============================================================ \033[0m')
    done()

# 创建浏览器


def run(playwright, config, index):
    # 账号列表
    accounts = config['list']
    # 是否所有账户都转账完毕
    if len(accounts) == index:
        # 结束脚本
        done()
    else:
        # 获取账户
        account = accounts[index]
        # 设置状态
        account['msg'] = '进行中...'
        # 输出日志
        output_log()
        # 开始转账，创建浏览器
        browser = playwright.chromium.launch(headless=bool(args.headless))
        # 新建窗口
        content = browser.new_context()
        # 新建页面
        page = content.new_page()
        # 访问登录
        try:
            page.goto('https://payeer.com/en/auth/')
        except:
            print(
                '\033[1;31m=========================== logs =========================== \033[0m')
            print('访问登录页失败！请检查网络环境！')
            print(
                '\033[1;31m============================================================ \033[0m')
            done()
        # 延迟
        page.wait_for_timeout(1000)
        # 写入账号
        page.fill('//input[@tabindex="1"]', account['account'])
        # 写入密码
        page.fill('//input[@tabindex="2"]', account['password'])
        # 点击登录
        page.click('//button[@tabindex="3"]')
        # 延迟
        page.wait_for_timeout(1000)
        # 切换到转钱
        page.click('//li[@class="transfer"]/a')
        # 延迟
        page.wait_for_timeout(1000)
        # 获取账户余额
        balance_str = page.locator(
            '//button[@id="btn-amount"]//s').text_content()
        balance = float(balance_str)
        # 记录余额，统计总金额
        account['balance'] = balance
        # 余额可以进行转账
        if balance > 0:
            # 填写转入账户
            page.fill('//input[@name="param_ACCOUNT_NUMBER"]',
                      config['account'])
            # 填写转入金额
            page.fill('//input[@name="sum_pay"]', balance_str)
            # 延迟
            page.wait_for_timeout(1000)
            # 移除焦点
            page.click('//div[contains(text(), "Total")]')
            # 延迟
            page.wait_for_timeout(1000)
            # 点击转入
            page.click('//button[contains(text(), "Send")]')
            # 延迟
            page.wait_for_timeout(1000)
            # 获取结果
            msg = page.locator('//div[@class="note_txt"]').text_content()
            # 判断结果
            if 'successfully' in msg:
                # 转账成功
                config['amount'] += balance
                # 设置状态
                account['msg'] = '成功'
            else:
                # 设置状态
                account['msg'] = '失败'
            # 输出日志
            output_log()
            # 关闭浏览器
            logout(browser, content, page)
            # 下一个账户
            run(playwright, config, index + 1)
        else:
            # 设置状态
            account['msg'] = '余额不足'
            # 输出日志
            output_log()
            # 关闭浏览器
            logout(browser, content, page)
            # 下一个账户
            run(playwright, config, index + 1)


# 调用
with sync_playwright() as playwright:
    # 跑起来
    run(playwright, config, 0)
