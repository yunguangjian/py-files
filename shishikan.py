# -*- coding: utf-8 -*-
import time
import os
import pyautogui
import xlrd
import win32gui
import pyperclip
import win32con
jb = win32gui.FindWindow(0, '基层店管理系统')  # 引号内输入要切换的窗口名称
win32gui.ShowWindow(jb, 1)  # 应对窗口最小化情况
win32gui.SetForegroundWindow(jb)  # 激活窗口至最前1，仅能激活
win32gui.SetWindowPos(jb, win32con.HWND_TOP, 448, 137, 1016, 775, win32con.SWP_SHOWWINDOW)  # 调整窗口在屏幕位置和大小
print(pyautogui.position())