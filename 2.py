# -*- coding: utf-8 -*-
import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
import re
import time
baseurl='http://m.54mn.cc/m/10999/1.html'
resp=requests.get(baseurl)
soup = BeautifulSoup(resp.text,"html.parser")
baseimg=soup.find_all('div',class_='index_c_img')
ym=str(soup.find_all('div',class_='index_c_page')[0])[-12:-10]
img_url=re.findall(r'src="(.*)"/></a>',str(baseimg))[0]
rs=img_url.rsplit("/",1)[1].split('.')[0]
img_url=re.findall(r'src="(.*)"/></a>',str(baseimg))[0].rsplit("/",1)[0]+'/'

print(f'总共{ym}张，开始')

async def download(url):
    name=url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(url) as resp2:
            with open('123/'+name,'wb') as f:
                f.write(await resp2.content.read())
                print(name)


async def main():
    tasks=[]
    for i in range(int(rs),int(ym)+int(rs)):
        url=img_url+str(i)+'.jpg'
        tasks.append(download(url))
    await asyncio.wait(tasks)
if __name__ == '__main__':
    ts=time.time()
    asyncio.run(main())
    print(time.time()-ts)