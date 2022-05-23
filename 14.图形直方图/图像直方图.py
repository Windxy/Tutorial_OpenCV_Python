import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    '''1.灰度直方图'''
    # 输入表示：原图、通道、Mask、BIN数目，范围
    img = cv2.imread('img/tiger.jpg',0) # 如果设置为1，就是灰度直方图
    '''返回的参数hist是一个3x256的一维数组'''
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.plot(hist)
    plt.show()
    # 或者是np中的histogram来进行直方图的运算
    # hist,bins = np.histogram(img.ravel(),256,[0,256])

    '''2.三通道直方图'''
    img = cv2.imread('img/tiger.jpg',1)
    bgr=['b','g','r']
    for i,color in enumerate(bgr):
        hist = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    cv2.imshow('img',img)
    plt.show()

    '''利用numpy进行掩膜运算得到直方图'''
    # mask = np.zeros(img.shape[:2],np.uint8)
    # mask[100:200,300:400]=255
    # mask_img = cv2.bitwise_and(img,img,mask)
    # hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
    # hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
    # plt.subplot(221), plt.imshow(img, 'gray')
    # plt.subplot(222), plt.imshow(mask,'gray')
    # plt.subplot(223), plt.imshow(mask_img, 'gray')
    # plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
    # plt.xlim([0,256])
    # plt.show()

    '''3.直方图均衡化'''
    img = cv2.imread('img/tiger.jpg',0)
    equ = cv2.equalizeHist(img)
    res = np.hstack((img,equ))
    #stacking images side-by-side
    cv2.imshow('res.png',res)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)
    res2 = np.hstack((img,cl1))
    cv2.imshow('res1.png',res2)


    '''4.2D直方图'''
    #如果要绘制颜色直方图，需要将图像的颜色空间从BGR转换到HSV
    #计算以为直方图，要从BGR转为HSV
    img = cv2.imread('img/tiger.jpg')
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #channels为H、S两个通道，H通道为180，S通道为256
    #取值范围H通道从0到180，S通道为0到256
    hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
    #numpy中也有相关函数，histogram2d，详见书
    #绘制直方图
    plt.imshow(hist,interpolation='nearest')
    plt.show()

    '''5.直方图反向投影'''
    roi = cv2.imread('img/tiger_roi.png')
    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    target = cv2.imread('img/tiger.jpg')
    hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
    # calculating object histogram
    roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
    # normalize histogram and apply backprojection
    # 归一化：原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
    #cv2.NORM_MINMAX 对数组的所有值进行转化，使它们线性映射到最小值和最大值之间
    # 归一化之后的直方图便于显示，归一化之后就成了 0 到 255 之间的数了。
    cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1) # Now convolute with circular disc
    # 此处卷积可以把分散的点连在一起
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dst = cv2.filter2D(dst,-1,disc)
    # threshold and binary AND
    ret,thresh = cv2.threshold(dst,50,255,0) # 别忘了是三通道图像，因此这里使用 merge 变成 3 通道
    thresh = cv2.merge((thresh,thresh,thresh))
    # 按位操作
    res = cv2.bitwise_and(target,thresh)
    res = np.hstack((target,thresh,res))

    # 显示图像
    cv2.imshow('1',res)

    cv2.waitKey(0)
