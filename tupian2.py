# -*- coding: utf-8 -*-
import os
from PIL import Image
import pyautogui
pj=[]
wz=0
fileName = os.listdir(r'C:\Users\Administrator\Desktop\123')

for i in fileName:
    if '主视图' in i or '右视图' in i:
        temp=fileName.pop(wz)
        pj.append(temp)
    wz=wz+1

    pdyj=['主视图','右视图','后视图','左视图','俯视图','仰视图','立体图']
    pd=i[i.find('图')-2:i.find('图')+1]
    if not pd in pdyj:
        pyautogui.alert('"'+i+'"'+'命名有问题，请检查')
        exit(0)
zs='{:0>3}'.format(pyautogui.prompt('请问是第几组图片？'))
fileName=pj+fileName

sst_height=963
zhu_width=0
you_width=0

for img in fileName:
    imagePath = os.path.join(r'C:\Users\Administrator\Desktop\123', img)
    print(img)
    pic = Image.open(imagePath)
    yxs=pic.size
    if '主视图' in img:
        height = sst_height
        zhb=height/yxs[1]
        width = round(yxs[0]*zhb)
        zhu_width =width
        img = img.replace('主视图', '1主视图')
    elif '右视图' in img:
        height = sst_height
        zhb=height/yxs[1]
        width = round(yxs[0]*zhb)
        you_width =width
        img = img.replace('右视图', '4右视图')
    elif '后视图' in img:
        height = sst_height
        width = zhu_width
        img = img.replace('后视图', '2后视图')
    elif '左视图' in img:
        height = sst_height
        width = you_width
        img = img.replace('左视图', '3左视图')
    elif '俯视图' in img:
        height = you_width
        width = zhu_width
        img = img.replace('俯视图', '5俯视图')
    elif '仰视图' in img:
        height = you_width
        width = zhu_width
        img = img.replace('仰视图', '6仰视图')
    elif '立体图1' in img:
        height = sst_height
        zhb=height/yxs[1]
        width = round(yxs[0]*zhb)
        img = img.replace('立体图1', '7立体图1')
    elif '立体图2' in img:
        height = sst_height
        zhb=height/yxs[1]
        width = round(yxs[0]*zhb)
        img = img.replace('立体图2', '8立体图2')
    elif '立体图3' in img:
        height = sst_height
        zhb=height/yxs[1]
        width = round(yxs[0]*zhb)
        img = img.replace('立体图3', '9立体图3')

    newpic = pic.resize((width, height),Image.ANTIALIAS)
    img=zs+img
    newpic = newpic.convert('RGB')
    newpic.save(r"C:\Users\Administrator\Desktop\456\{}.jpg".format(img[:-4]),dpi=(300.0,300.0))