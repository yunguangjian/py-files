# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageEnhance
import os
import PIL.ImageOps
import pyautogui

imagesDirectory = r"C:\Users\Administrator\Desktop\123"
xz=pyautogui.confirm(text='增强亮度请按1，反转颜色请按2',buttons=['1','2'])
if xz in '1':
    for imageName in os.listdir(imagesDirectory):
        imagePath = os.path.join(imagesDirectory, imageName)
        image = Image.open(imagePath)
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(1.5)
        enh_con = ImageEnhance.Contrast(image)
        image=enh_con.enhance(1.5)
        image.save(r"C:\Users\Administrator\Desktop\456\{}".format(imageName))
elif xz in '2':
    for imageName in os.listdir(imagesDirectory):
        imagePath = os.path.join(imagesDirectory, imageName)
        image = Image.open(imagePath)
        image=PIL.ImageOps.invert(image)
        image.save(r"C:\Users\Administrator\Desktop\456\{}".format(imageName))