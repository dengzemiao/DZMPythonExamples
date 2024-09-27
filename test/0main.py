# pip install pygetwindow
import pygetwindow as gw
# pip install pywin32
import win32gui

def runWin32pro (text):
    # 找到的窗口区域
    found_region = None
    # 枚举所有窗口
    def enum_windows(hwnd, results):
        nonlocal found_region
        window_text = win32gui.GetWindowText(hwnd)
        window_class = win32gui.GetClassName(hwnd)
        # if text in window_class:  # 假设微信窗口类名包含 WeChat
        #     rect = win32gui.GetWindowRect(hwnd)
        #     print(f"窗口位置: (Left: {rect[0]}, Top: {rect[1]})")
        #     print(f"窗口大小: (Width: {rect[2] - rect[0]}, Height: {rect[3] - rect[1]})")
        if text in window_text:  # 假设微信窗口类名包含 WeChat
            rect = win32gui.GetWindowRect(hwnd)
            # print(f"窗口位置: (Left: {rect[0]}, Top: {rect[1]})")
            # print(f"窗口大小: (Width: {rect[2] - rect[0]}, Height: {rect[3] - rect[1]})")
            found_region = (rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])
            print(f"Region for pywin32: {found_region}")
            # return False  # 返回 False 以停止枚举
    # 开始枚举所有窗口
    win32gui.EnumWindows(enum_windows, None)
    return found_region

def runWin32 (text):
    # 枚举所有窗口
    def enum_windows(hwnd, results):
        window_text = win32gui.GetWindowText(hwnd)
        window_class = win32gui.GetClassName(hwnd)
        # if text in window_class:  # 假设微信窗口类名包含 WeChat
        #     rect = win32gui.GetWindowRect(hwnd)
        #     print(f"窗口位置: (Left: {rect[0]}, Top: {rect[1]})")
        #     print(f"窗口大小: (Width: {rect[2] - rect[0]}, Height: {rect[3] - rect[1]})")
        if text in window_text:  # 假设微信窗口类名包含 WeChat
            rect = win32gui.GetWindowRect(hwnd)
            # print(f"窗口位置: (Left: {rect[0]}, Top: {rect[1]})")
            # print(f"窗口大小: (Width: {rect[2] - rect[0]}, Height: {rect[3] - rect[1]})")
            region = (rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])
            print(f"Region for pywin32: {region}")
    # 开始枚举所有窗口
    win32gui.EnumWindows(enum_windows, None)

def runpywin (text):
    # 获取所有窗口的标题
    windows = gw.getAllTitles()
    # 查找窗口
    for title in windows:
        if text in title:  # 窗口标题中包含 "微信"
            view_window = gw.getWindowsWithTitle(title)[0]
            # 打印窗口的位置信息和大小
            # print(f"窗口位置: (Left: {view_window.left}, Top: {view_window.top})")
            # print(f"窗口大小: (Width: {view_window.width}, Height: {view_window.height})")
            # 可以将这些值用于 pyautogui 的截图操作
            region = (view_window.left, view_window.top, view_window.width, view_window.height)
            print(f"Region for pyautogui: {region}")

if __name__ == '__main__':
    runWin32pro('【水哥哥】壁纸定时更换器')
    # runWin32('【水哥哥】壁纸定时更换器')
    # runpywin('【水哥哥】壁纸定时更换器')
