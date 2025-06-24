# -*- coding: utf-8 -*-
# import pandas as pd
#
# fhdf=pd.read_excel(io=r'C:\Users\Administrator\Desktop\香香\test\test.XLS')
# mfdf=pd.read_excel(io=r'C:\Users\Administrator\Desktop\香香\test\test.XLS',sheet_name=1)
# njdf=pd.read_excel(io=r'C:\Users\Administrator\Desktop\香香\test\test.XLS',sheet_name=2)
#
# fhdf=fhdf.loc[:,'期号':'总册数']
# fhdf=pd.merge(fhdf,mfdf,left_on='销货店',right_on='店名')
# del fhdf['店名']
# hbdf=fhdf.groupby(['店号','期号','序号','销货店','书名','定价'])['总册数'].sum().reset_index()
# hbdf=pd.merge(hbdf,njdf,on='书名')
# hbdf.sort_values(by=['店号','期号','序号'],inplace=True,ascending=[True,True,True])
#
# print(hbdf)
# hbdf.to_excel(r'C:\Users\Administrator\Desktop\123.xls',index=0)
import pyautogui
wz=pyautogui.position()
print(wz)
pyautogui.hotkey('alt','tab')
pyautogui.moveTo(1264,464)
for i in range(1000):
    pyautogui.click()