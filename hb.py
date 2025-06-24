# -*- coding: utf-8 -*-
import os

path = r"D:\py files\123"        # 文件夹目录
files = os.listdir(path)     # 得到文件夹下的所有文件名称


for file in files:  # 遍历文件
    f = open(path+"\\"+file,encoding='utf-8').read()  # 将打开的文件内容保存到变量f
    log = open(path+"\\"+'全知读者视角.log', 'a+',encoding='utf-8')  # 以追加模式打开文件
    log.write(f)                     # 写入文件
    print('已经合并：' + file)