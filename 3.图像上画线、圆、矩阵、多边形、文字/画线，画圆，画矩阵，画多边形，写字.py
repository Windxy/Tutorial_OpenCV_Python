import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('img\\tiger.jpg', 1)

    # 作矩阵
    cv2.rectangle(img, (10, 9), (281, 127), (0, 255, 0), 2)

    # 画线，从img的10，10位置画到100，100位置,粗细为2
    cv2.line(img, (10, 10), (100, 100), color=(255, 0, 0), thickness=2)

    # 圆的话只需要指定半径和圆心
    cv2.circle(img, (50, 50), 50, (0, 0, 255), 2)

    # 画多边形
    pts = np.array([[100, 100], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (255, 255, 0), 2)

    # 写字
    cv2.putText(img, r"Hello OpenCV", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
    cv2.imshow('img', img)
    cv2.waitKey(0)
