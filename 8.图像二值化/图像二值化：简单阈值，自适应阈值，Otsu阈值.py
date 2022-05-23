import cv2
img = cv2.imread('img/fish.png', 0)

if __name__ == '__main__':

    # 1.简单阈值
    # 第四个参数可更改
    ret,thread=cv2.threshold(img,126,245,cv2.THRESH_BINARY)

    # 2.自适应阈值
    img = cv2.medianBlur(img,5)
    _,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    #11 为 Block size, 2 为 C 值
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    # 3.OTSU阈值
    ret3,th3 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    while(1):
        cv2.imshow('src',img)
        cv2.imshow('img_th1',thread)
        cv2.imshow('img_th2',th2)
        cv2.imshow('img_th3',th3)
        if cv2.waitKey(1)& 0xFF==27:
            break