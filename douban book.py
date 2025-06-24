# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt

def main():
    baseurl="https://book.douban.com/top250?start="
    #1.爬取网页
    datalist=getData(baseurl)
    savepath="豆瓣读书top250.xls"
    #3.保存数据
    saveData(datalist,savepath)
    # askURL("https://book.douban.com/top250?start=0")
#影片链接的规则
findlink = re.compile(r'<a class="nbg" href="(.*)"')         #创建正则表达式对象，表示规则（字符串的模式）
#影片图片
findimgsrc = re.compile(r'<img .*src="(.*?)".*?',re.S)
#影片片名
findtitle = re.compile(r'title="(.*)">')
#影片评分
findrating =re.compile(r'<span class="rating_nums">(.*)</span>')
#评价人数
findnum =re.compile(r'<span class="pl">(\d*)人评价</span>',re.S)
#找到概况
findInq=re.compile(r'<span class="inq">(.*)</span>',re.S)
#找到影片相关
findbd = re.compile(r'<p class="pl">(.*)</p>',re.S)
#爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        url =baseurl +str(i*25)
        html=askURL(url)
        #2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('tr',class_="item"):       #查找符合要求的字符串，形成列表
            # print(item)  #测试查看电影item全部信息
            data=[] #保存一部电影的信息
            item = str(item)
            #影片详情的链接
            link = re.findall(findlink,item) [0]        #re库用来通过正则表达式查找指定的字符串
            data.append(link)
            print(link)


            imgsrc = re.findall(findimgsrc, item)[0]
            data.append(imgsrc)

            title =re.findall(findtitle,item)
            if(len(title)==2):
                ctitle=title[0]
                data.append(ctitle)
                otitle=title[1].replace("/","")         #去掉/号
                data.append((otitle))
            else:
                data.append(title)
                data.append(' ')    #外国名字留空

            rating = re.findall(findrating,item)[0]
            data.append(rating)

            num = re.findall(findnum,item)[0]
            data.append(num)

            inq = re.findall(findInq,item)
            if len(inq)!=0:
                inq= inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")


            bd = re.findall(findbd, item)[0]
            bd = re.sub('br(/s+)?/>'," ",bd)    #去掉br
            bd = re.sub('/'," ",bd)
            data.append(bd.strip())     #去掉空格

            datalist.append(data)       #将处理好的一部电影信息放入datalist


    return datalist
#得到一个指定url的网页内容
def askURL(url):
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"}
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
#保存数据
def saveData(datalist,savepath):
    book =xlwt.Workbook(encoding="uft-8",style_compression=0)
    sheet = book.add_sheet('豆瓣读书250',cell_overwrite_ok=True)
    col =("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])         #列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save('豆瓣读书250.xls')


if __name__ == '__main__':       #当程序执行时
    main()
