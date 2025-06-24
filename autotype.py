# -*- coding: utf-8 -*-
import time
import os
import pyautogui
import xlrd
import win32gui
import pyperclip
import win32con

try:
    # 此方法为尝试读取传送列表列表，再尝试py免费列表，如果都不行，只能用粘贴列表的方法！
    #先尝试的情形

    wb=xlrd.open_workbook(r'E:\香香\传送列表\lbtemp.xlsx')#注意修改路径！
    sht=wb.sheets()[0]
    lx=sht.cell_value(0,5)
    b=sht.cell_value(1,5)[2:]
    a=eval(b)
    print(a)
except:
    #再尝试的情形，一般适用情形为ERP学免互转,此种方法可以批量！请注意
    # 免费调整专用#########################################################################################################################
    try:
        wb = xlrd.open_workbook(r'E:\香香\2022秋免费\py免费列表.xlsx')  # 注意修改路径！
        for i in range(-1,-31,-1):#根据实际学校所在标签填写
            sht = wb.sheets()[i]
            b = sht.cell_value(1, 13)[2:]
            a = eval(b)
            jb = win32gui.FindWindow(0, '基层店管理系统')  # 引号内输入要切换的窗口名称
            win32gui.ShowWindow(jb, 1)  # 应对窗口最小化情况
            win32gui.SetForegroundWindow(jb)  # 激活窗口至最前1，仅能激活
            win32gui.SetWindowPos(jb, win32con.HWND_TOP, 448, 137, 1016, 775, win32con.SWP_SHOWWINDOW)  # 调整窗口在屏幕位置和大小
            for _ in range(4):
                pyautogui.typewrite(['tab'])
            pyautogui.typewrite(sht.cell_value(1,0))
            for _ in range(4):
                pyautogui.typewrite(['tab'])
            pyautogui.typewrite('01')
            for _ in range(2):
                pyautogui.typewrite(['tab'])
            pyautogui.typewrite(['enter'])
            # time.sleep(2)#根据实际时间调整
            pyautogui.typewrite(['tab'])
            for xh in a:
                pyautogui.typewrite(xh, 0.05)
            pyautogui.typewrite(['tab'])
            pyautogui.typewrite(['tab'])
            pyautogui.typewrite(['enter'])
            pyautogui.typewrite(['enter'])
            time.sleep(2)
            pyautogui.click(x=1205, y=341)
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('f2')
        pyautogui.keyUp('ctrlleft')
    #########################################################################################################################################
    except:
    # 粘贴改免费列表
         a=[['tab'],['tab'],['tab'],['tab'],'664',['tab'],['tab'],['tab'],['tab'],'01',['tab'],['tab'],['enter'],['tab'],'179',['down'],'179',['down'],'179',['down'],'7',['down'],'172',['down'],'7',['down'],'172',['down'],'179',['down'],'179',['down'],'218',['down'],'-39',['down'],'179',['down'],'220',['down'],'-41',['down'],'9',['down'],'170',['down'],'9',['down'],'170',['down'],'9',['down'],'170',['down'],'218',['down'],'-39',['down']]




try:
    # 通常为激活ERP系统句柄至最前来实现切换窗口，如果系统没打开，则运用alt+tab来切换窗口
    jb=win32gui.FindWindow(0,'基层店管理系统')       #引号内输入要切换的窗口名称
    win32gui.ShowWindow(jb,1)                      #应对窗口最小化情况
    win32gui.SetForegroundWindow(jb)                #激活窗口至最前1，仅能激活
    win32gui.SetWindowPos(jb,win32con.HWND_TOP,448,137,1016,775,win32con.SWP_SHOWWINDOW)        #调整窗口在屏幕位置和大小
except:
    pyautogui.keyDown('altleft');
    pyautogui.press('tab');
    pyautogui.keyUp('altleft')            #此方法为运用alt+tab来切换窗口


if not os.path.exists('sbcs.txt'):
    sbcs=open('sbcs.txt','w+')
    pyautogui.alert('第一次运行，请确认初始坐标！')
    pyautogui.alert('请把鼠标放到“学生数”位置，并按“空格”确认')
    xsds= str(pyautogui.position()[0:2])
    pyautogui.alert('请把鼠标放到“免费数”位置，并按“空格”确认')
    mfds= str(pyautogui.position()[0:2])
    pyautogui.alert('请把鼠标放到“学生折扣”位置，并按“空格”确认')
    xszk= str(pyautogui.position()[0:2])
    sbcs.write(f'{xsds}\n{mfds}\n{xszk}')
    sbcs.close()
sbcs=open('sbcs.txt','r+')
lb=sbcs.readlines()
xsds=eval(lb[0])
mfds=eval(lb[1])
xszk=eval(lb[2])
sbcs.close()


def hc(n):
  for n in range(0,n):
    pyautogui.typewrite(['enter'], 0.05)

def xx(n):
    pyautogui.typewrite(str(a[n]), 0.02)
    hc(1)

def zt(n):
    pyautogui.alert('书名：'+str(a[n+1])+chr(10)+ '数量：' +str(a[n+3]))

def ds(n):
    pyautogui.typewrite(str(a[n+3]), 0.01)

def zk(n):
    pyautogui.typewrite(str(a[n + 4]), 0.01)
    hc(1)

def xh(n):
    pyautogui.typewrite(str(a[n + 5]), 0.01)

def mx(n):
    pyautogui.alert('书名：'+ str(a[n+3])+chr(10)+ '出版年月：' +str(a[n+4]))

def pd(n):
    pyautogui.typewrite(str(a[n+2]), 0.01)


n=0


if '\n' in a:
  for i in a:
    pyautogui.typewrite(i,0.1)
# ['down']为ERP学免互转
elif ['down'] in a:
  for i in a:
    pyautogui.typewrite(i, 0.03)
elif '鼠标' in a:
  for i in range(0, len(a), 5):
    xx(i)
    time.sleep(0.7)
    if int(a[i+2])==2:
        pyautogui.moveTo(mfds, duration=0.01)#用注释方法获得鼠标点击位置
        pyautogui.click()
        ds(i)
        hc(int(a[i+4]))
    else:
        if int(a[i]) in [760,761,770,771,991]:
            zk = pyautogui.prompt('请输入折扣',default=100)
            win32gui.SetForegroundWindow(jb)
            pyautogui.moveTo(xsds, duration=0.01)  # 用注释方法获得鼠标点击位置
            pyautogui.click()
            ds(i)
            pyautogui.moveTo(xszk, duration=0.01)
            pyautogui.click()
            pyautogui.moveRel(110, 0)
            pyautogui.doubleClick()
            pyautogui.typewrite(zk,0.01)
            hc(1)
            pyautogui.moveTo(xszk, duration=0.01)
            pyautogui.click()
            pyautogui.moveTo(xsds, duration=0.01)
            pyautogui.moveRel(0, -25)
            pyautogui.click()
        else:
            pyautogui.moveTo(xsds, duration=0.01)  # 用注释方法获得鼠标点击位置
            pyautogui.click()
            ds(i)
            hc(int(a[i + 4]))
elif '添单' in a:
  for i in range(0,len(a),6):
      xx(i)
      time.sleep(0.3)
      xh(i)
      hc(3)
      zt(i)
      win32gui.SetForegroundWindow(jb)
      pyperclip.copy(a[i+3])
      pyautogui.hotkey('ctrl', 'v')
      hc(1)
      zk(i)
      time.sleep(0.2)
elif '中盘' in lx:
    for i in range(0, len(a), 6):
        xx(i)
        if int(a[i+1])==2:
            hc(1)
        mx(i)
        pyautogui.moveTo(x=784, y=849)
        win32gui.SetForegroundWindow(jb)
        pyautogui.click()
        pd(i)
        hc(1)
        xh(i)
        hc(1)
elif '报废' in lx:
    for i in range(0, len(a), 4):
        xx(i)
        if int(a[i+1])==2:
            hc(1)
        pyautogui.alert(str('书名：'+a[i + 2]) + chr(10) +'数量：'+ str(a[i + 3]))
        win32gui.SetForegroundWindow(jb)
        ds(i)
        hc(3)
elif '转移' in lx:
    for i in range(0, len(a), 4):
        xx(i)
        if int(a[i+1])==2:
            hc(1)
        pyautogui.alert(str('书名：'+a[i + 2]) + chr(10) +'数量：'+ str(a[i + 3]))
        win32gui.SetForegroundWindow(jb)
        ds(i)
        hc(1)