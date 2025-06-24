# -*- coding: utf-8 -*-
import pyautogui
import win32gui
import win32con
import time
import pyperclip
a=("030000004162TD","030000004170TD","030000004171TD","030000004172TD","030000004173TD","030000004174TD","030000004175TD","030000004176TD","030000004177TD","030000004178TD","030000004179TD","030000004180TD","030000004181TD","030000004182TD","030000004183TD","030000004184TD","030000004185TD","030000004186TD")
pycharm = win32gui.GetForegroundWindow()  # 换取pycharm句柄
win32gui.ShowWindow(pycharm, win32con.SW_SHOWMINNOACTIVE)  # pycharm最小化
jb = win32gui.FindWindow(0, '基层店管理系统')  #
win32gui.ShowWindow(jb, 1)  # 应对窗口最小化情况
win32gui.SetForegroundWindow(jb)  # 激活窗口至最前1，仅能激活
win32gui.SetWindowPos(jb, win32con.HWND_TOP, 448, 137, 1016, 775, win32con.SWP_SHOWWINDOW)  # 调整窗口在屏幕位置和大小
for i in a:
    pyautogui.moveTo(830,280)
    pyautogui.doubleClick()
    pyperclip.copy(i)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press(['tab'])
    pyautogui.press(['tab'])
    pyautogui.press(['enter'])
    time.sleep(15)
    pyautogui.moveTo(830,280)
    pyautogui.doubleClick()
    pyautogui.press(['tab'])
    pyautogui.press(['enter'])
    pyautogui.press(['enter'])
    time.sleep(1)
    pyautogui.hotkey('alt','f4')