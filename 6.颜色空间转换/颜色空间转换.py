import cv2

if __name__ == '__main__':

    src = cv2.imread("img/tiger.jpg")
    cv2.namedWindow("rgb", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("rgb", src)

    # RGB to HSV
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv", hsv)

    # RGB to YUV
    yuv = cv2.cvtColor(src, cv2.COLOR_BGR2YUV)
    cv2.imshow("yuv", yuv)

    # RGB to YCrCb
    ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
    cv2.imshow("ycrcb", ycrcb)

    src2 = cv2.imread("img/tiger.jpg")
    cv2.imshow("src2", src2)
    hsv = cv2.cvtColor(src2, cv2.COLOR_BGR2HSV)
    # 获取掩膜
    mask = cv2.inRange(hsv, (35, 43, 46), (99, 255, 255))
    cv2.imshow("mask", mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

