# -*- coding: utf-8 -*-
import requests
from  lxml import etree
import aiohttp
import asyncio


async def download(url,ym):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            tree = etree.HTML(await resp.text())
            bt = tree.xpath('//*[@id="mlfy_main_text"]/h3/text()')[0]
            nr = tree.xpath('//*[@id="mlfy_main_text"]/div[2]//text()')
            nr = ' '.join(nr)
            ym = "{0:04d}".format(ym)
            with open(f'123/{ym}.txt', 'w+', encoding='utf-8') as f:
                f.write(bt)
                f.write(nr)
                print(bt + '已完成')
async def main():
    tasks=[]
    for ym in range(900,1308):
        url = baseurl + str(ym) + '.html'
        tasks.append(download(url,ym))
    await asyncio.wait(tasks)
if __name__ == '__main__':
    baseurl = 'https://www.xsohuo.com/chapter/114782/'
    asyncio.run(main())