import cv2
import numpy as np

if __name__ == '__main__':

    img = cv2.imread('img/XT.png', 0)
    kernel = np.ones((17,17),np.uint8)
    # 膨胀
    test1 = cv2.erode(img,kernel=kernel)
    # 腐蚀
    test2 = cv2.dilate(img,kernel=kernel)
    # 开运算
    test3 = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel=kernel)
    # 闭运算
    test4 = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel=kernel)
    # 形态学梯度 膨胀-腐蚀
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    # 礼帽 原始图像与进行开运算之后得到的图像的差。
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    # 黑帽 进行闭运算之后得到的图像与原始图像的差
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    while(1):
        cv2.imshow('src',img)
        cv2.imshow('test1',test1)
        cv2.imshow('test2',test2)
        cv2.imshow('test3', test3)
        cv2.imshow('test4',test4)
        cv2.imshow('gradient',gradient)
        cv2.imshow('test6',tophat)
        cv2.imshow('test7',blackhat)
        if cv2.waitKey(0) & 0xFF==27:
            break
