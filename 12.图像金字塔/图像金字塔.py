import cv2

if __name__ == '__main__':
    img = cv2.imread('img/tiger.jpg')
    lower_reso = cv2.pyrDown(img)
    cv2.imshow('lower_img',lower_reso)
    high_reso = cv2.pyrUp(lower_reso)
    cv2.imshow('Up_img',high_reso)
    cv2.waitKey(0)