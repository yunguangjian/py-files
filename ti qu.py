# -*- coding: utf-8 -*-
from pathlib import Path
import xlwt
pt=r'C:\Users\Administrator\Desktop\123'
wb = xlwt.Workbook(encoding = 'utf-8')
sht=wb.add_sheet("文件名转表")
path = Path(pt)
sht.write(0,0,'设备名称')
sht.write(0,1,'厚度')
sht.write(0,2,'零件编码')
sht.write(0,3,'数量')

n=1
for sub_file in path.glob("**/*.*"):
    wjdz=str(sub_file).split('\\')
    dw=wjdz.index('123')
    sht.write(n, 0, wjdz[dw + 1])
    sht.write(n, 1, wjdz[dw + 2])
    sht.write(n, 2, wjdz[dw + 3][:-4])
    sht.write(n, 3, wjdz[dw + 3][wjdz[dw + 3].find('（')+1:wjdz[dw + 3].find('）')])
    n=n+1
wb.save(pt[:-3]+r'456\文件名转表.xls')