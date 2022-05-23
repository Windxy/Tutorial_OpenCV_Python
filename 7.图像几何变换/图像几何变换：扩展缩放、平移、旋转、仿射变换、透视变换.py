import cv2
import numpy as np
img = cv2.imread('img/tiger.jpg')

if __name__ == '__main__':

    #1 缩放，推荐cv2.INTER_AREA，扩展推荐v2.INTER_CUBIC，cv2.INTER_LINEAR，默认cv2.INTER_LINEAR
    '''resize函数'''
    res=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)

    #2 平移
    '''warpAffine函数，接收2x3矩阵，前两列固定，后两列是平移长度'''
    Mat = np.float32([[1,0,100],[0,1,50]])
    res2=cv2.warpAffine(img,Mat,(300,300))

    #3 旋转
    # 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
    # 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
    '''getRotationMatrix2D函数，接收3x3矩阵'''
    rows,cols=img.shape[:2]
    M=cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)
    res3=cv2.warpAffine(img,M,(300,300))

    #4 仿射变换
    '''getAffineTransform()函数，图像前的三个点，图像后的三个点，形成仿射变换'''
    pts1=np.float32([[50,50],[150,50],[50,200]])
    pts2=np.float32([[10,100],[50,50],[50,250]])
    M1=cv2.getAffineTransform(pts1,pts2)
    res4=cv2.warpAffine(img,M1,(cols,rows))

    #5 透视变换
    '''getPerspectiveTransform()函数，需要2个参数，图像前4个点，图像后4个点，一般用来矫正图像'''
    img2=cv2.imread('img/book.jpg')
    res5=img
    rows,cols,ch=img.shape
    pts3 = np.float32([[56,65],[131,52],[28,387],[389,390]])    # 矫正前的四个点
    pts4 = np.float32([[0,0],[300,0],[0,300],[300,300]])        # 矫正后的四个点
    M2=cv2.getPerspectiveTransform(pts3,pts4)
    res5=cv2.warpPerspective(res5,M2,(600,600))

    while(1):
        cv2.imshow('src', img)
        cv2.imshow('1',res)
        cv2.imshow('2',res2)
        cv2.imshow('3',res3)
        cv2.imshow('4',res4)
        cv2.imshow('5',res5)
        if cv2.waitKey(1) & 0xFF==27:
            break