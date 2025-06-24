# -*- coding: utf-8 -*-
import win32gui
import win32con
import pyautogui
import time
jb = win32gui.FindWindow(0, '基层店管理系统')  # 引号内输入要切换的窗口名称
win32gui.ShowWindow(jb, 1)  # 应对窗口最小化情况
win32gui.SetForegroundWindow(jb)  # 激活窗口至最前1，仅能激活
win32gui.SetWindowPos(jb, win32con.HWND_TOP, 448, 137, 1016, 775, win32con.SWP_SHOWWINDOW)  # 调整窗口在屏幕位置和大小
def wait_for_color(x, y, target_color, timeout=30):
    """等待指定坐标的颜色变为目标颜色"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        current_color = pyautogui.pixel(x, y)
        if current_color == target_color:
            return True
        time.sleep(0.5)
    raise TimeoutError(f"坐标({x},{y})颜色未变为{target_color}")


for _ in range(4):
    pyautogui.typewrite(['tab'])
pyautogui.typewrite('604')
for _ in range(4):
    pyautogui.typewrite(['tab'])
pyautogui.typewrite('01')
for _ in range(2):
    pyautogui.typewrite(['tab'])
pyautogui.typewrite(['enter'])
# 示例：等待提交按钮变为可点击状态（颜色变化）
wait_for_color(x=1029, y=335, target_color=(204, 204, 204))
pyautogui.prompt('123')