# -*- coding: utf-8 -*-
import pyautogui
import win32gui
import win32api
import time
import pyperclip
import os
import math
from pyautocad import Autocad,APoint
from pathlib import Path
import xlwt
import tkinter as tk
from tkinter import filedialog
ja=pyautogui.confirm(text='请确保打开CAD后，再点击“确定”！ '+chr(13)+'本套图是否为“佳安”',buttons=['是','否'])
dxx=win32api.GetKeyState(20)
if dxx==0:
    pyautogui.press('capslock')
imagesDirectory = r"C:\Users\Administrator\Desktop\123"
path = Path(imagesDirectory)
for sub_file in path.glob("**/"):#开始检查456文件夹是否存在123文件夹中的子文件夹，没有就创建
    if not os.path.exists(str(sub_file).replace(r'\123',r'\456')):
        os.mkdir(str(sub_file).replace(r'\123',r'\456'))#检查结束
def callback(hwnd, hwnd_list):
    hwnd_title = win32gui.GetWindowText(hwnd)
    if target_title in hwnd_title:
        hwnd_list.append(hwnd)
hwnd_list = []
target_title='CAD 2020'
win32gui.EnumWindows(callback, hwnd_list)
zs=0
cw=0
js=0
cwlb=[]
for wj in path.glob("**/*.*"):
    zs=zs+1
for wj in path.glob("**/*.*"):
    js=js+1
    x = []
    y = []
    os.startfile(str(wj))#打开CAD文件
    time.sleep(3)#等待秒数
    acad = Autocad(create_if_not_exists=True)#连接CAD
    pyperclip.copy(str(wj).split('\\')[-1][:-4])#复制文件名
    pyautogui.middleClick()
    pyautogui.middleClick()
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
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
        wzzxwz=APoint(max(x) - (max(x) - min(x)) / 2, max(y) - (max(y) - min(y)) / 2)
        if max(x)-min(x)>=max(y)-min(y):
            text.Move(wzwz,wzzxwz)
        else:
            text.Move(wzwz,wzzxwz)
            text.Rotate(wzzxwz, math.pi / 2)  # 旋转90度
        if ja in '是':
            if str(wj).find('10mm')!=-1:
                pyautogui.moveTo(643, 324)
                zbwz = pyautogui.confirm(text='是否调整文字位置'+chr(13)+f'本次共需运行{zs}个文件，当前为第{js}个', buttons=[ '取消','缩放','调整'])
                if zbwz in '取消':
                    pass
                elif zbwz in '缩放':
                    sfbl=pyautogui.prompt('请输入缩放比例',default=0)
                    text.ScaleEntity(wzzxwz,float(sfbl))
                else:
                    text.Move(wzzxwz,APoint(acad.doc.Utility.Getpoint(APoint(0,0), "请选取一个点")))
        else:
            pyautogui.moveTo(607, 320)
            zbwz = pyautogui.confirm(text='是否调整文字位置' + chr(13) + f'本次共需运行{zs}个文件，当前为第{js}个', buttons=['缩放', '调整'])
            if zbwz in '缩放':
                sfbl = pyautogui.prompt('请输入缩放比例', default=0)
                text.ScaleFactor = int(sfbl)
            else:
                text.Move(wzzxwz, APoint(acad.doc.Utility.Getpoint(APoint(0, 0), "请选取一个点")))
        acad.doc.SaveAs(str(wj).replace(r'\123',r'\456')[:-4])  # 文件另存
    except:
        cw=cw+1
        cwlb.append(str(wj))
        pyautogui.hotkey('ctrl', 'f4')  # 关闭当前文件
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.press('enter')
    else:
        pyautogui.hotkey('ctrl','f4')  # 关闭当前文件
        pyautogui.press('enter')
        time.sleep(1)
        os.remove(str(wj))#删除123文件夹dwg文件
xz=pyautogui.confirm(text=f'本次共运行文件{zs}个,出现问题{cw}个，是否需要导出问题文件路径',buttons=['是','否'])
if xz in '是':
    wb = xlwt.Workbook(encoding='utf-8')
    sht = wb.add_sheet("错误列表")
    for r in range(len(cwlb)):
        sht.write(r,0,cwlb[r])
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    # 打开文件对话框
    file_path = filedialog.asksaveasfilename(title='选择保存路径和文件名', defaultextension=".xls")
    if len(file_path)==0:
        pyautogui.alert('导出失败')
    else:
        wb.save(file_path)