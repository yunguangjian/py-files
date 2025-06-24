# -*- coding: utf-8 -*-
import xlrd
import os
import pyautogui
import pyperclip
import win32gui
import win32con
pyautogui.alert('请确认ERP系统是否仅按顺序打开“订数按书导入”和“已确认订数修改”')
jb = win32gui.FindWindow(0, '基层店管理系统')  # 引号内输入要切换的窗口名称
win32gui.ShowWindow(jb, 1)  # 应对窗口最小化情况
win32gui.SetForegroundWindow(jb)  # 激活窗口至最前1，仅能激活
win32gui.SetWindowPos(jb, win32con.HWND_TOP, 448, 137, 1016, 775, win32con.SWP_SHOWWINDOW)  # 调整窗口在屏幕位置和大小
lj=r'E:\香香\传送列表'#注意修改路径！
wjlb=os.listdir(lj)
bj=0
for wjm in wjlb:
    if not wjm  in '免费与非免费传送列表.xlsm':
        pyautogui.click(1414, 306)
        wj=os.path.join(lj,wjm)
        wb=xlrd.open_workbook(wj)
        sht=wb.sheets()[0]
        zklb=sht.col_values(5)[1:]
        qh=wjm.split('-')[0]
        xh = wjm.split('-')[1]
        for cf in range(6):
            pyautogui.press('tab')
        pyautogui.hotkey('ctrl','a')
        pyautogui.typewrite(qh)
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(xh)
        pyautogui.press('enter')
        for cf in range(5):
            pyautogui.press('tab')
        pyautogui.press('enter')
        pyperclip.copy(wj)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        for cf in range(5):
            pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('enter')
        n=1
        if len(zklb)!=zklb.count(''):
            pyautogui.hotkey('ctrl', 'tab')
            for zk in zklb:
                if zk !=100 and len(str(zk))>0:
                    pyautogui.click(1309, 314)
                    for cf in range(12):
                        pyautogui.press('tab')
                    pyautogui.typewrite(str(int(sht.cell_value(n,0))))
                    for cf in range(3):
                        pyautogui.press('tab')
                    pyautogui.typewrite(qh)
                    for cf in range(2):
                        pyautogui.press('tab')
                        pyautogui.typewrite(xh)
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    for cf in range(16):
                        pyautogui.press('tab')
                    pyautogui.typewrite(str(sht.cell_value(n, 5)))
                    for cf in range(10):
                        pyautogui.press('tab')
                    pyautogui.press('enter')
                    pyautogui.press('enter')
                n=n+1
            pyautogui.hotkey('ctrl', 'tab')