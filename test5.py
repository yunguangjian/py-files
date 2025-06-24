# -*- coding: utf-8 -*-
import cv2

t1 = 0
t2 = 0


def Preview(img_path, ts1, ts2):
    img = cv2.imread(img_path)
    img_copy = img.copy()

    imgCanny = cv2.Canny(img, ts1, ts2)

    g = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    g2 = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

    img_dilate = cv2.dilate(imgCanny, g)
    img_dilate2 = cv2.dilate(imgCanny, g2)

    shape = img_dilate.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            if img_dilate2[i, j] == 0:
                img[i, j] = [0, 0, 0]

    cv2.namedWindow("Preview", cv2.WINDOW_NORMAL)
    cv2.createTrackbar("kerner_size", "Preview", 0, 7, nothing)
    while (1):
        size = cv2.getTrackbarPos("kerner_size", "Preview")
        dst = cv2.GaussianBlur(img, (2 * size + 1, 2 * size + 1), 0, 0, cv2.BORDER_DEFAULT)

        for i in range(shape[0]):
            for j in range(shape[1]):
                if img_dilate[i, j] != 0:
                    img_copy[i, j] = dst[i, j]

        cv2.imshow("Result", img_copy)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    cv2.destroyAllWindows()


def Choose_Thre(img_path):
    global t1, t2
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow("Preview", cv2.WINDOW_NORMAL)

    def nothing(WEV):
        pass

    cv2.createTrackbar("Threshold1", "Preview", 0, 255, nothing)
    cv2.createTrackbar("Threshold2", "Preview", 0, 255, nothing)
    while (1):
        t1 = cv2.getTrackbarPos("Threshold1", "Preview")
        t2 = cv2.getTrackbarPos("Threshold2", "Preview")
        detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
        detected_edges = cv2.Canny(detected_edges, t1, t2, apertureSize=3)
        dst = cv2.bitwise_and(img, img, mask=detected_edges)
        cv2.imshow('Edge', dst)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()


def nothing(wte):
    pass


# 按esc退出 直接关闭无效
img_path = r"C:\Users\Administrator\Desktop\123\5.jpg"
Choose_Thre(img_path)
print(t1, t2)
Preview(img_path, t1, t2)
