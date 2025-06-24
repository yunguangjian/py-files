# -*- coding: utf-8 -*-
import pyautogui
import win32gui
import win32con
import time
import pyperclip
a=("102","103","104","105","106","108","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","129","201","202","203","204","205","206","207","208","210","211","212","213","214","215","216","217","218","219","220","221","222","223","224","225","226","227","228","229","230","231","232","233","234","235","236","237","238","239","240","241","242","243","245","246","251","252","253","254","256","258","259","260","261","262","263","264","265","266","267","269","270","271","272","301","302","304","305","306","307","308","309","310","311","312","313","314","315","316","317","318","319","604","608","609","610","612","613","621","626","627","630","635","645","652","653","654","659","660","661","662","664","710","717","740","741","751","752","753","754","755","756","759","760","761","770","771","780","781")
pycharm = win32gui.GetForegroundWindow()  # 换取pycharm句柄
win32gui.ShowWindow(pycharm, win32con.SW_SHOWMINNOACTIVE)  # pycharm最小化
jb = win32gui.FindWindow(0, '基层店管理系统')  #
win32gui.ShowWindow(jb, 1)  # 应对窗口最小化情况
win32gui.SetForegroundWindow(jb)  # 激活窗口至最前1，仅能激活
win32gui.SetWindowPos(jb, win32con.HWND_TOP, 448, 137, 1016, 775, win32con.SWP_SHOWWINDOW)  # 调整窗口在屏幕位置和大小
for i in a:
    pyperclip.copy(i)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press(['tab'])
    pyautogui.press(['enter'])
    pyautogui.press(['tab'])
    pyautogui.press(['enter'])
    pyautogui.press(['enter'])
    pyautogui.press(['enter'])
    time.sleep(1)
    pyautogui.press(['tab'])
    pyautogui.press(['tab'])
    pyautogui.press(['tab'])
    pyautogui.press(['tab'])
    pyautogui.press(['tab'])
    time.sleep(1)