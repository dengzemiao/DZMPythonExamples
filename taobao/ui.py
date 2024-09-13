import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("简单的 Tkinter 界面")
root.geometry("300x200")

# 标签
label = tk.Label(root, text="请输入您的名字:")
label.pack(pady=10)

# 输入框
entry = tk.Entry(root)
entry.pack(pady=5)

# 按钮点击事件
def on_button_click():
    name = entry.get()
    if name:
        messagebox.showinfo("信息", f"你好, {name}!")
    else:
        messagebox.showwarning("警告", "请输入名字！")

# 按钮
button = tk.Button(root, text="提交", command=on_button_click)
button.pack(pady=10)

# 运行主循环
root.mainloop()
