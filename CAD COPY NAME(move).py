# -*- coding: utf-8 -*-
import os



import pyautogui
import win32gui
import win32api
import time
import pyperclip
import os
import math
from pyautocad import Autocad,APoint
pyautogui.alert('请确保打开CAD后，再点击“确定”！')
dxx=win32api.GetKeyState(20)
if dxx==0:
    pyautogui.press('capslock')
imagesDirectory = r"C:\Users\Administrator\Desktop\123"
bl=os.listdir(imagesDirectory)
def callback(hwnd, hwnd_list):
    hwnd_title = win32gui.GetWindowText(hwnd)
    if target_title in hwnd_title:
        hwnd_list.append(hwnd)
hwnd_list = []
target_title='CAD 2020'
win32gui.EnumWindows(callback, hwnd_list)
for wj in bl:
    bj=0
    x=[]
    y=[]
    os.startfile(imagesDirectory + '\\' + wj)#打开CAD文件
    time.sleep(3)#等待秒数
    acad = Autocad(create_if_not_exists=True)#连接CAD
    pyperclip.copy(wj[:-4])#复制文件名
    pyautogui.middleClick()
    pyautogui.middleClick()
    pyautogui.hotkey('ctrl','v')
    pyautogui.click()
    time.sleep(1)
    try:
        for text in acad.iter_objects('Text'):
            text.AttachmentPoint = 5#设置对正为左中

            wzwz = APoint(text.InsertionPoint)  # 获取文字位置
        for line in acad.iter_objects('Line'):
            x.append(line.StartPoint[0])
            x.append(line.EndPoint[0])
            y.append(line.StartPoint[1])
            y.append(line.EndPoint[1])
        for circle in acad.iter_objects('Circle'):
            x.append(circle.Center[0]+circle.Radius)
            x.append(circle.Center[0] - circle.Radius)
            y.append(circle.Center[1]+circle.Radius)
            y.append(circle.Center[1]-circle.Radius)
        if max(x)-min(x)>=max(y)-min(y):
            text.Move(wzwz,APoint(max(x) - (max(x) - min(x)) / 2, max(y) - (max(y) - min(y)) / 2))
        else:
            text.Move(wzwz,APoint(max(x) - (max(x) - min(x)) / 2, max(y) - (max(y) - min(y)) / 2))
            text.Rotate(APoint(max(x) - (max(x) - min(x)) / 2, max(y) - (max(y) - min(y)) / 2), math.pi / 2)  # 旋转90度
        acad.doc.SaveAs(imagesDirectory[:-3]+r"456\{}".format(wj[:-4]))  # 文件另存
    except:
        pyautogui.alert(wj+'读取有问题，现将关闭，运行下一个文件')
        pyautogui.hotkey('ctrl', 'f4')  # 关闭当前文件
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.press('enter')
    else:
        pyautogui.hotkey('ctrl','f4')  # 关闭当前文件
        pyautogui.press('enter')
        time.sleep(1)
        os.remove(imagesDirectory + '\\' + wj)#删除123文件夹dwg文件