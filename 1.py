# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time
import openpyxl
import pyautogui
from openpyxl.styles import PatternFill
# baseurl='http://q.quantuwang1.com/m/63569c4bafcfb73a.html'
# resp=requests.get(baseurl)
# soup = BeautifulSoup(resp.text,"html.parser")
# baseimg=soup.find_all('div',class_='index_c_img')
# ym=str(soup.find_all('div',class_='index_c_page')[0])[-12:-10]
# img_url=re.findall(r'src="(.*)1.jpg"/></a>',str(baseimg))[0]
# rs=img_url.rsplit("/",1)[1].split('.')[0]
# img_url=re.findall(r'src="(.*)"/></a>',str(baseimg))[0].rsplit("/",1)[0]+'/'
#
# print(f'总共{ym}张，开始')
# ts=time.time()
# for i in range(int(rs),int(ym)+int(rs)):
#     url=img_url+str(i)+'.jpg'
#     resp2=requests.get(url)
#     with open(f'123/{i}.jpg','wb') as f:
#         f.write(resp2.content)
#         print(str(i)+'完成')
# print(time.time()-ts)
# print('完毕')
# a=['我是',1,2,3]
# a.pop()
# print(type(len(a)))
# 原始字符串，包含中文括号
import re

# 示例字符串
text = "这里是(（123)）中文·测试"

# 正则表达式匹配数字、中文和点号
pattern = r'[\d·]+|[\u4e00-\u9fff]+'

# 查找所有匹配项
matches = re.findall(pattern, text)
print(matches)