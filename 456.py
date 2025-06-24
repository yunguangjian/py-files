# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import time
base_url='https://www.bige7.com'
ml_url='https://www.bige7.com/book/1031'
ml_resp=requests.get(ml_url)
ml_resp.encoding='uft-8'
soup=BeautifulSoup(ml_resp.text,'html.parser')
zj = soup.find_all('div',class_="listmain")
zj_jq=re.findall(r'<dd><a href="(/.*).html">(.*)</a></dd>',str(zj))
ts=time.time()
for zj_url, zj_bt in zj_jq:
    url = base_url + zj_url + '.html'
    name = zj_bt.replace('</a></dd><dd class="more pc_none"><a href="javascript:dd_show()" rel="nofollow">&lt;&lt;---展开全部章节---&gt;&gt;','')
    resp=requests.get(url)
    nc = str(re.findall(r'<div id="chaptercontent" class="Readarea ReadAjax_content">(.*)', resp.text)[0]).replace(r'<br /><br />', '\n')
    with open(f'123/{name}.txt', 'w', encoding='utf-8') as f:
        f.write(nc)
        print(name)
print(time.time()-ts)