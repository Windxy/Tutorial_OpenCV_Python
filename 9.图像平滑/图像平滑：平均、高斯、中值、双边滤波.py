import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread('img/tiger.jpg')
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
plt.subplot(231),plt.imshow(img),plt.title('src'),plt.xticks([]),plt.yticks([])

def gasuss_noise(image, mean=0, var=0.001):
    '''
        添加高斯噪声
        image:原始图像
        mean : 均值
        var : 方差,越大，噪声越大
    '''
    image = np.array(image/255, dtype=float)#将原始图像的像素值进行归一化，除以255使得像素值在0-1之间
    noise = np.random.normal(mean, var ** 0.5, image.shape)#创建一个均值为mean，方差为var呈高斯分布的图像矩阵
    out = image + noise#将噪声和原始图像进行相加得到加噪后的图像
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)#clip函数将元素的大小限制在了low_clip和1之间了，小于的用low_clip代替，大于1的用1代替
    out = np.uint8(out*255)#解除归一化，乘以255将加噪后的图像的像素值恢复
    cv2.imshow("gasuss", out)
    noise = noise*255
    return [noise,out]

if __name__ == '__main__':

    # 平滑主要用于消除图像中的高频分量，但不影响低频分量，实际用于消除噪声，或在提取较大的目标前去除太小的细节或将目标内的小间断连接起来。
    #均值
    img2 = gasuss_noise(image=img)
    # cv2.imshow('noise',img2)
    cv2.waitKey(0)
    blur= cv2.blur(img,(3,3))
    plt.subplot(232),plt.imshow(blur),plt.title('blur'),plt.xticks([]),plt.yticks([])

    #高斯
    Gaussi=cv2.GaussianBlur(img,(5,5),0)
    plt.subplot(233),plt.imshow(Gaussi),plt.title('Gaussian'),plt.xticks([]),plt.yticks([])

    #中值滤波
    median = cv2.medianBlur(img,5)
    plt.subplot(234),plt.imshow(median),plt.title('median'),plt.xticks([]),plt.yticks([])

    #双边滤波
    bilateralFilter = cv2.bilateralFilter(img,9,75,75)
    plt.subplot(235),plt.imshow(bilateralFilter),plt.title('bilateralFilter'),plt.xticks([]),plt.yticks([])

    plt.show()