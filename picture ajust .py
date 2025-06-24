# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import os
imagesDirectory = r"C:\Users\Administrator\Desktop\123"
fg = 200
if len(os.listdir(imagesDirectory[:-3]+'456'))==0:
    for imageName in os.listdir(imagesDirectory):
        imagePath = os.path.join(imagesDirectory, imageName)
        image = Image.open(imagePath)
        # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
        Img = image.convert('L')
        ia=np.array(Img)
        df=np.where(ia<fg,0,ia)
        df=np.where(ia>=fg,255,df)
        tp=Image.fromarray(df)
        tp.save(imagesDirectory[:-3]+'456'+'\\'+imageName)
else:
    for imageName in os.listdir(imagesDirectory[:-3]+'456'):
        imagePath = os.path.join(imagesDirectory, imageName)
        image = Image.open(imagePath)
        # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
        Img = image.convert('L')
        ia=np.array(Img)
        df=np.where(ia<fg,0,ia)
        df=np.where(ia>=fg,255,df)
        tp=Image.fromarray(df)
        tp.save(imagesDirectory[:-3]+'456'+'\\'+imageName)