import numpy as np
import cv2

if __name__ == '__main__':

    src = cv2.imread('img/dog2.jpg')
    img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    # 1.寻找轮廓findContours
    ret,threah = cv2.threshold(img,127,255,0)
    _,contours,_ = cv2.findContours(threah,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    res = cv2.drawContours(src,contours,1058,(0,0,255),2)

    cv2.imshow('gray_img',img)
    cv2.imshow('res',res)
    # cv2.waitKey(0)

    cnt = contours[1058]
    M = cv2.moments(cnt)
    print(M)

    # 2.重心
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print("重心",cx,cy)

    # 3.面积
    area = cv2.contourArea(cnt)
    print("面积",area)

    # 4.周长
    perimeter = cv2.arcLength(cnt,True)
    print("周长",perimeter)

    # 5.轮廓近似
    epsilon = 0.1*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True) #  Douglas-Peucker algorithm
    vertexes = approx.shape[0]
    if vertexes == 3:
        cv2.putText(src, "triangle", (np.int32(cx), np.int32(cy)),
                   cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8)
    if vertexes == 4:
        cv2.putText(src, "rectangle", (np.int32(cx), np.int32(cy)),
                   cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8)
    if vertexes == 6:
        cv2.putText(src, "poly", (np.int32(cx), np.int32(cy)),
                   cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8)
    if vertexes > 10:
        cv2.putText(src, "circle", (np.int32(cx), np.int32(cy)),
                   cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8)
    print(vertexes)

    # 6.凸包
    hull = cv2.convexHull(cnt)
    # print("凸包",hull)

    # 7.凸性检测
    k = cv2.isContourConvex(cnt)#False说明不是凸性
    print("凸性检测（False说明不是凸性）",k)

    # 8.直矩阵
    x,y,w,h = cv2.boundingRect(cnt)
    src_2 = src.copy()
    img = cv2.rectangle(src_2,(x,y),(x+w,y+h),(100,255,0),2)
    cv2.imshow('img_b',img)

    # 9.旋转矩阵
    x,y,w,h = cv2.boundingRect(cnt)
    src_3 = src.copy()
    img = cv2.rectangle(src_3,(x,y),(x+w,y+h),(100,0,250),2)
    cv2.imshow('img_c',img)

    # 10.最小外接圆
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))#cv2.namedWindow('image')
    radius = int(radius)
    src_4 = src.copy()
    img = cv2.circle(src_4,center,radius,(100,240,0),2)
    cv2.imshow('img_r',img)

    # 11.椭圆拟合
    (cx, cy), (a, b), angle = cv2.fitEllipse(cnt)
    src_5 = src.copy()
    img = cv2.ellipse(src_5, (np.int32(cx), np.int32(cy)),
                   (np.int32(a/2), np.int32(b/2)), angle, 0, 360, (0, 0, 255), 2, 8, 0)
    cv2.imshow('img_i',img)

    # 12.直线拟合
    cols = img.shape[1]
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    src_6 = src.copy()
    img = cv2.line(src_6,(cols-1,righty),(0,lefty),(0,255,0),2)
    cv2.imshow('img_i',img)

    cv2.waitKey(0)
