import cv2
import numpy as np
# 第一个坐标：631,470
# 第一个坐标：719,471
# 第一个坐标：322,690
# 第二个坐标：1069,706

if __name__ == '__main__':

    #5 透视变换
    '''getPerspectiveTransform()函数，需要2个参数，图像前4个点，图像后4个点，一般用来矫正图像'''
    img = cv2.imread('img/rode2.jpg')
    res = img
    rows, cols, ch = img.shape
    print(rows,cols)
    # cv2.circle(img,(322,690),5,(0,0,255),2)
    # cv2.circle(img,(1069,706),5,(0,0,255),2)
    # pts3 = np.float32([[631,470],[719,471],[296,715],[1088,716]])    # 矫正前的四个点
    # pts4 = np.float32([[0,0],[300,0],[0,600],[300,600]])        # 矫正后的四个点
    pts3 = np.float32([[536,430],[614,430],[233,707],[1097,707]])    # 矫正前的四个点
    pts4 = np.float32([[0,0],[300,0],[0,600],[300,600]])        # 矫正后的四个点
    M2=cv2.getPerspectiveTransform(pts3,pts4)
    res5=cv2.warpPerspective(res,M2,(300,600))

    # cv2.circle(img,(0,0),50,(0,0,255),2)
    # cv2.circle(img,(cols,0),50,(0,0,255),2)
    # cv2.circle(img,(0,rows),50,(0,0,255),2)
    # cv2.circle(img,(cols,rows),50,(0,0,255),2)


    while(1):
        cv2.imshow('src', img)
        cv2.imshow('1',res5)
        if cv2.waitKey(1) & 0xFF==27:
            break