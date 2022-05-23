import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread('img/line_.png')
cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 目标追踪
cap = cv2.VideoCapture('img/lane.avi')
cv2.namedWindow('frame')

#设置多边形掩膜:
def define_poly_mask():
    b = np.array([[[333, 342], [194, 422], [638, 437], [516, 346]]], dtype=np.int32)
    im = np.zeros((480,856), dtype="uint8")
    cv2.polylines(im, b, 1, 255)
    cv2.fillPoly(im, b, 255)
    mask_ = im
    return mask_

mask_ = define_poly_mask()

# 通过掩膜方式得到ROI区域
while(cap.isOpened()):

    ret, frame = cap.read()
    # 设置白色阈值
    lower_ = np.array([0, 0,100])
    upper_ = np.array([120 , 50, 240])
    # 构建掩膜
    # print(hsv.shape[:2])
    cv2.imshow('src',frame)
    cv2.imshow('mask_',mask_)
    # 位运算相与
    final=cv2.bitwise_and(frame,frame,mask=mask_)
    cv2.imshow('frame', final)

    # 转换为hsv
    hsv = cv2.cvtColor(final, cv2.COLOR_BGR2HSV)
    mask_1 = cv2.inRange(hsv, lower_, upper_)

    ans = cv2.bitwise_and(hsv,hsv,mask=mask_1)
    cv2.imshow('ans',ans)

    img = final
    bgr = ['b', 'g', 'r']
    for i, color in enumerate(bgr):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    cv2.imshow('img', img)
    # plt.show()
    plt.pause(0.01)
    plt.clf()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# 如何找需要的HSV，用cvtColor即可
def How_to_find_HSV():
    start=np.uint8(np.array([[[90,90,100]]]))
    end=np.uint8(np.array([[[110,110,120]]]))
    start_hsv=cv2.cvtColor(start,cv2.COLOR_BGR2HSV)
    end_hsv=cv2.cvtColor(end,cv2.COLOR_BGR2HSV)
    print(start_hsv,end_hsv)