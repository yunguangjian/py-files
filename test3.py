# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
imagesDirectory = r"C:\Users\Administrator\Desktop\123"

for imageName in os.listdir(imagesDirectory):
    imagePath = os.path.join(imagesDirectory, imageName)
    # 读取图片
    image = cv2.imread(imagePath)

    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用阈值进行二值化
    _, mask = cv2.threshold(gray,200,255, cv2.THRESH_BINARY)

    # 对掩膜进行膨胀和腐蚀，去除噪声
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = cv2.erode(mask, kernel, iterations=1)

    # 将掩膜反转，得到前景和背景
    mask = cv2.bitwise_not(mask)

    # 将掩膜应用到原图，得到抠图
    item = cv2.bitwise_and(image, image, mask=mask)

    # 显示图片
    # cv2.imshow('Original', image)
    # cv2.imshow('Mask', mask)
    # cv2.imshow('Item', item)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 保存抠图
    cv2.imwrite(r"C:\Users\Administrator\Desktop\456\{}".format(imageName), item)
