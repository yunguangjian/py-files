# -*- coding: utf-8 -*-
import asyncio
import requests
import aiohttp
from lxml import etree
async def downlaod(img_url):
    name=img_url.rsplit('/',1)[1].split('.')[0]
    async with aiohttp.ClientSession() as session:
        async with session.get(img_url) as img_con:
            with open(f'123/{name}.jpg','wb') as f:
                f.write(await img_con.content.read())
                print(name)
async def main(qs_url):
    tasks=[]
    qs_resp = requests.get(qs_url)
    tree = etree.HTML(qs_resp.text)
    img_urls = tree.xpath('/html/body/table[2]/tr/td/table/tr/td/a/@href')
    for img_url in img_urls:
        tasks.append(downlaod(img_url))
    await asyncio.wait(tasks)




if __name__ == '__main__':

    qs_url='http://beautyleg.com/photo/show.php?no=115'
    asyncio.run(main(qs_url))
