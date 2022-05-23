import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread('img/tiger.jpg',1)

if __name__ == '__main__':

    # A.对老虎图片像素进行修改
    # print(img) # img格式是ndarray，因此可以对其进行像素级修改

    # 将bgr转化为hsv
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img = img.astype(np.float)
    # 获取v通道（颜色亮度通道），并做渐变性的增强
    img[:, :, 2] = np.where(img[:, :, 2] > 100, img[:, :, 2] + 10.0, img[:, :, 2])
    img[:, :, 2] = np.where(img[:, :, 2] > 150, img[:, :, 2] + 10.0, img[:, :, 2])
    img[:, :, 2] = np.where(img[:, :, 2] > 180, img[:, :, 2] + 40.0, img[:, :, 2])
    # 令大于255的像素值等于255（防止溢出）
    img = np.where(img > 255, 255, img)
    img = img.astype(np.uint8)
    res = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow('res', res)
    cv2.waitKey(0)

    img[140:150,200:270,0:3]=0      #3个通道，对应图像长款[140:150,200:270]全部设置为0
    img[:,:,:1]=0                   #通道顺序是BGR顺序
    cv2.imshow('img',img)

    # B.获取图像属性
    print("像素总数:"+str(img.size)+"\n图像数据类型:"+str(img.dtype)+"\n图像大小"+str(img.shape))

    # C.图像ROI
    eye = img[140:150,200:270,0:3]

    # D.拆分及合并图像通道
    b=img[:,:,0]    #img的第1个通道
    g=img[:,:,1]    #img的第2个通道
    r=img[:,:,2]    #img的第3个通道
    # 或使用cv2.split()
    b_,g_,r_=cv2.split(img) #分离img的3个通道
    # img = merge(b_,g_,r_)

    # E.图像填充
    BLUE=[0,0,255]
    img1=cv2.imread('img/tiger.jpg',1)
    replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)   #边界填充
    reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
    constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

    plt.subplot(231),plt.imshow(img1,),plt.title('Original')
    plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
    plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
    plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('relect_101')
    plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
    plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')
    plt.show()

    cv2.waitKey(0)