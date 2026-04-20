import tkinter as tk
from time import strftime

# 窗口移动
def start_move(event):
    root.x = event.x
    root.y = event.y
    root.attributes("-alpha", 0.9)

def stop_move(event):
    root.attributes("-alpha", 0.7)

def on_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

# 退出
def exit_clock(event):
    root.destroy()

# 更新时间
def time():
    current = strftime("%Y-%m-%d %H:%M:%S")
    lbl.config(text=current)
    lbl.after(1000, time)

# 窗口设置
root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-alpha", 0.7)
root.geometry("350x80")

# 样式
lbl = tk.Label(root, font=("微软雅黑", 20, "bold"),
               bg="black", fg="white")
lbl.pack(fill=tk.BOTH, expand=True)

# 绑定
lbl.bind("<Button-1>", start_move)
lbl.bind("<ButtonRelease-1>", stop_move)
lbl.bind("<B1-Motion>", on_move)
lbl.bind("<Button-3>", exit_clock)

time()
root.mainloop()