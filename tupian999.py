from PIL import Image
from PIL import ImageEnhance
import numpy as np
import os

imagesDirectory = r"C:\Users\Administrator\Desktop\123"  # tiff图片所在文件夹路径

i = 0
for imageName in os.listdir(imagesDirectory):
    imagePath = os.path.join(imagesDirectory, imageName)
    image = Image.open(imagePath)  # 打开tiff图像
    ImageArray = np.array(image)
    zq_img = ImageEnhance.Contrast(image).enhance(factor=1.1) # 增强图片对比度，原图参数为1
    ImageArray = np.array(zq_img)
    row = ImageArray.shape[0]
    col = ImageArray.shape[1]

    # 先计算所有图片的裁剪范围，然后再统一裁剪并输出图片
    x_left = row
    x_top = col
    x_right = 0
    x_bottom = 0
    # 上下左右范围
    """
    Image.crop(left, up, right, below)
    left：与左边界的距离
    up：与上边界的距离
    right：还是与左边界的距离
    below：还是与上边界的距离
    简而言之就是，左上右下。
    """
    i += 1
    pd_left = 0
    pd_top = 0
    pd_right = 0
    pd_bottom = 0
    rgb=252**3
    for r in range(row):
        if pd_top==1:
            break
        for c in range(col):
            if int(ImageArray[r][c][0]) * int(ImageArray[r][c][1]) * int(ImageArray[r][c][2]) <= rgb:
                x_top =r
                pd_top=1
                break
    for r in range(row-1,-1,-1):
        if pd_bottom==1:
            break
        for c in range(col):
            if int(ImageArray[r][c][0]) * int(ImageArray[r][c][1]) * int(ImageArray[r][c][2]) <= rgb:
                x_bottom =r
                pd_bottom=1
                break
    for c in range(col):
        if pd_left==1:
            break
        for r in range(row):
            if int(ImageArray[r][c][0]) * int(ImageArray[r][c][1]) * int(ImageArray[r][c][2])<= rgb:
                x_left =c
                pd_left=1
                break
    for c in range(col-1,-1,-1):
        if pd_right==1:
            break
        for r in range(row):
            if int(ImageArray[r][c][0]) * int(ImageArray[r][c][1]) * int(ImageArray[r][c][2])<= rgb:
                x_right =c
                pd_right=1
                break

    print(x_left, x_top, x_right, x_bottom)
    # image = Image.open(imagePath)  # 打开tiff图像
    cropped = image.crop((x_left - 0, x_top - 0, x_right + 0, x_bottom + 0))  # (left, upper, right, lower)
    cropped.save(r"C:\Users\Administrator\Desktop\456\{}".format(imageName, i),dpi=(300.0,300.0))
    print("imageName completed!")