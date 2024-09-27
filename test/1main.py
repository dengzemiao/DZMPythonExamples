import pyautogui
# import easyocr
from PIL import Image
import win32gui

# 获取微信窗口的句柄和位置
def get_wechat_window():
    hwnds = []
    
    # 枚举所有窗口
    def enum_windows(hwnd, lParam):
        window_text = win32gui.GetWindowText(hwnd)
        window_class = win32gui.GetClassName(hwnd)
        # 假设微信窗口类名包含 "WeChat"
        if "WeChat" in window_class:
            hwnds.append(hwnd)

    win32gui.EnumWindows(enum_windows, None)

    if hwnds:
        hwnd = hwnds[0]  # 如果找到多个微信窗口，选择第一个
        rect = win32gui.GetWindowRect(hwnd)  # 获取窗口矩形 (left, top, right, bottom)
        return rect
    else:
        print("微信窗口未找到")
        return None

# 截图微信窗口并保存
def screenshot_wechat_window():
    rect = get_wechat_window()
    if rect:
        # 截图的区域
        left, top, right, bottom = rect
        width = right - left
        height = bottom - top
        region = (left, top, width, height)

        # 使用 pyautogui 截图
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save("wechat_screenshot.png")
        return screenshot
    return None

# 识别微信聊天内容
# def recognize_text_from_screenshot(screenshot):
#     # 初始化 EasyOCR 模型
#     reader = easyocr.Reader(['ch', 'en'])  # 支持中文和英文
    
#     # OCR 识别图片中的文字
#     results = reader.readtext('wechat_screenshot.png')

#     print("识别到的聊天内容：")
#     for result in results:
#         print(result[1])  # 输出识别到的文本

# 主流程
screenshot = screenshot_wechat_window()
# if screenshot:
#     recognize_text_from_screenshot(screenshot)
