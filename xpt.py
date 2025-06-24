# -*- coding: utf-8 -*-
from lxml import etree
import requests
import aiohttp
from bs4 import BeautifulSoup
import re
import asyncio
import os

async def download(lj,url):
    name=url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as sesion:
            async with sesion.get(url) as resp4:
                with open(f'123/{lj}/{name}','wb') as f:
                    f.write(await resp4.content.read())
                    print(name)


async def main():
    tasks=[]
    for url in tasks_url:
        lj=url.split(',')[0]
        url=url.split(',')[1]

        # print(url,lj)
        tasks.append(download(lj,url))
    await asyncio.wait(tasks)



if __name__ == '__main__':
    gf_url='http://q.quantuwang1.com/'#http://q.quantuwang1.com/
    base_url = ['http://q.quantuwang1.com/meinv/xiuren/']
    resp1=requests.get(base_url[0])
    tree=etree.HTML(resp1.text)
    fy=tree.xpath('/html/body/div[3]/div/div[4]/a/@href')

    for idx in fy:
        base_url.append(gf_url+idx)
    for base_xh in base_url:
        resp2=requests.get(base_xh)
        tree2 = etree.HTML(resp2.text)
        jc_url=tree2.xpath('/html/body/div[3]/div/div[2]/ul/li/a/@href')
        for qs_url in jc_url:
            tasks_url = []
            qs_url=gf_url+qs_url
            resp3=requests.get(qs_url)
            resp3.encoding='utf-8'
            soup = BeautifulSoup(resp3.text, "html.parser")
            baseimg = soup.find_all('div', class_='index_c_img')
            ym = str(soup.find_all('div', class_='index_c_page')[0])[-12:-10]
            wjj=soup.find_all('div', class_='index_c_title')
            img_url = re.findall(r'src="(.*)"/></a>', str(baseimg))[0]
            rs = img_url.rsplit("/", 1)[1].split('.')[0]
            img_url = re.findall(r'src="(.*)"/></a>', str(baseimg))[0].rsplit("/", 1)[0] + '/'
            wjjn=re.findall(r'<div class="index_c_title">(.*)</div>',str(wjj))[0]
            wjjn=wjjn.replace(r'/','-')
            if not os.path.exists(f"123/{wjjn}"):
                os.mkdir(f"123/{wjjn}")

            for i in range(int(rs), int(ym) + int(rs)):
                zjurl = img_url + str(i) + '.jpg'
                tasks_url.append((wjjn+','+zjurl))
            asyncio.run(main())