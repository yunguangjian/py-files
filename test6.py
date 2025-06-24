# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 读取图像
img = cv2.imread(r'C:\Users\Administrator\Desktop\123\5.jpg')

# 创建一个和图像同样大小的掩模，并用0填充（表示背景）
mask = np.zeros(img.shape[:2], np.uint8)

# 初始化ROI区域的位置和大小
r = cv2.selectROI(img, False)

# 根据选定的ROI创建掩模
mask[r[1]:r[1] + r[3], r[0]:r[0] + r[2]] = 1

# 设置grabCut参数
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
iterCount = 5

# 运行grabCut算法
cv2.grabCut(img, mask, bgdModel, fgdModel, iterCount, cv2.GC_INIT_WITH_MASK)

# 修改mask，使其只包含确定的物体区域
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# 将mask应用到原图
img = img * mask2[:, :, np.newaxis]

# 显示结果
cv2.imshow('grabCut result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()