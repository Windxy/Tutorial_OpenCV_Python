import cv2

if __name__ == '__main__':

    img=cv2.imread('img/XT.png', 0)
    #cv2.CV_64F 输出图像的深度（数据类型），可以使用-1, 与原图像保持一致 np.uint8
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    # 参数 1,0 为只在 x 方向求一阶导数，最大可以求 2 阶导数。
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
    # 参数 0,1 为只在 y 方向求一阶导数，最大可以求 2 阶导数。
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
    Canny = cv2.Canny(img,100,240)

    cv2.imshow('src',img)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobel_x',sobelx)
    cv2.imshow('sobel_y', sobely)
    cv2.imshow('Canny',Canny)
    cv2.waitKey(0)
