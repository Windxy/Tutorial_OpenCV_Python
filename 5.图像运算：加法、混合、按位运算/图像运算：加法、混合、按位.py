import cv2
import numpy as np

if __name__ == '__main__':

    # 1.加法
    img = np.zeros((500,500,1),np.uint8) # 全0
    color = np.ones((500,500,1),np.uint8)# 全1
    res = cv2.add(img,color)    # subtract减法  multiply乘法  divide()除法
    print(res)

    # 2.混合
    src1=cv2.imread('img/building01.jpg')
    src2 = cv2.imread('img/tiger.jpg')
    src2 = cv2.resize(src2,(384,288))

    dst=cv2.addWeighted(src1,0.7,src2,0.5,0)
    cv2.imshow('dst',dst)

    # 3.按位操作，一般用的很少
    dst1 = cv2.bitwise_and(src1, src2)
    dst2 = cv2.bitwise_xor(src1, src2)
    dst3 = cv2.bitwise_or(src1, src2)

    cv2.imshow("dst1", dst1)
    cv2.imshow("dst2", dst2)
    cv2.imshow("dst3", dst3)
    cv2.waitKey(0)