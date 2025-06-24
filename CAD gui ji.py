# -*- coding: utf-8 -*-
import pyautogui
import win32gui
import time
def callback(hwnd, hwnd_list):
    hwnd_title = win32gui.GetWindowText(hwnd)
    if target_title in hwnd_title:
        hwnd_list.append(hwnd)
hwnd_list = []
target_title='CAD 2020'
win32gui.EnumWindows(callback, hwnd_list)
n=0
gs = int(pyautogui.prompt('请输入本类个数'))+1
for xh in range(1,gs):
    win32gui.SetForegroundWindow(hwnd_list[0])
    pyautogui.hotkey('ctrl','a')
    pyautogui.typewrite('find')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.alert('请选择图形')
    pyautogui.hotkey('ctrl','x')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.alert('请确定完位置再继续')
    pyautogui.hotkey('ctrl','shift','tab')
    time.sleep(1)