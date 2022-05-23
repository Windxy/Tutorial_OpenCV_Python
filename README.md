# Tutorial_OpenCV_Python
一个简单易入门的Python+OpenCV教程



### 1.本教程环境配置

Python == 3.7

opencv-python == 3.4.2.16

opencv-contrib-python == 3.4.2.16



### 2.说明

|                    名称                     |                             概述                             |                             备注                             |
| :-----------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|              1.图像读写和显示               |    学习如何通过OpenCV读取图像，并进行显示，最后再进行保存    |      cv2.imread()<br />cv2.imshow()<br />cv2.imwrite()       |
|         2.读取视频或摄像头的图像帧          | 学习如何通过OpenCV读取视频或摄像头的图像帧，获取帧的帧率、图像宽高等信息 | cv2.VideoCapture()<br />cv2.release()<br />cv2.destroyAllWindows() |
|           3.图像上绘图和写入文字            | 学习如何通过OpenCV绘制常见图形，包括线、圆、矩形、多边形、字符 | cv2.line()<br />cv2.circle()<br />cv2.rectangle()<br />cv2.polylines()<br />cv2.putText() |
| 4.图像基础操作：像素、属性、ROI、通道、填充 | 学习如何通过OpenCV操作图像的像素、获取属性（包括类型、大小、尺寸）、拆分通道、获取ROI（感兴趣区域）、填充 | cv2.split()<br />cv2.copyMakeBorder()<br />cv2.size/dtype/shape |
|      5.图像运算：加法、混合、按位运算       | 学习如何通过OpenCV进行图像的加减乘除法、两个图像进行混合、按位运算 | cv2.add()<br />cv2.subtract()<br />cv2.multiply()<br />cv2.divide()<br />cv2.addWeighted()<br />cv2.bitwise_and()<br />cv2.bitwise_or()<br />cv2.bitwise_xor() |
|             6.图像颜色空间转换              | 学习如何通过OpenCV进行颜色空间转换，包括BRG、RGB、HSV、YUV、YCrCb、获取特定范围掩膜 |              cv2.cvtColor()<br />cv2.inRange()               |
|               7.图像几何变换                |  学习如何通过OpenCV进行缩放、平移、旋转、仿射变换、透视变换  | cv2.resize()<br />cv2.warpAffine()<br />cv2.warpPerspective()<br /> |
|                8.图像二值化                 | 学习如何通过OpenCV进行图像二值化，包括简单阈值、自适应阈值、Otsu阈值 |                       cv2.threshold()                        |
|                 9.图像平滑                  | 学习如何通过OpenCV进行图像平滑，包括均值滤波、高斯滤波、中值滤波、双边滤波 | cv2.blur()<br />cv2.GaussianBlur()<br />cv2.medianBlur()<br />cv2.bilateralFilter() |
|              10.图像形态学变换              | 学习如何通过OpenCV进行形态学变换，包括腐蚀、膨胀、开运算、闭运算、礼帽、黑帽等 |  cv2.erode()<br />cv2.dilate()<br />cv2.morphologyEx(<br />  |
|                 11.图像梯度                 | 学习如何通过OpenCV进行图像的梯度计算，包括Sobel算子、Canny算子、Laplacian算子 |      cv2.Laplacian()<br />cv2.Sobel()<br />cv2.Canny()       |
|                12.图像金字塔                |           学习如何通过OpenCV进行图像获取图像金字塔           |                cv2.pyrDown()<br />cv2.pyrUp()                |
|                 13.图像轮框                 | 学习如何通过OpenCV在二值图像中寻找轮廓；<br />获得轮廓的面积和周长；<br />轮廓近似；<br />轮廓凸包及凸性检测；<br />轮廓的最小外接直矩形、子最小外接旋转矩形和最小外接圆；<br />轮廓的椭圆和直线拟合 | cv2.drawContours()<br />cv2.moments()<br />cv2.contourArea()<br />cv2.arcLength()<br />cv2.approxPolyDP()<br />cv2.convexHull()<br />cv2.isContourConvex()<br />cv2.boundingRect()<br />cv2.minEnclosingCircle()<br />cv2.fitEllipse()<br />cv2.fitLine()<br />... |
|                14.图形直方图                | 学习如何通过OpenCV计算、绘制灰度和三通道直方图，直方图均衡化、2D直方图、直方图反向投影 | cv2.calcHist()<br />cv2.equalizeHist()<br />np.hstack()<br />cv2.calcBackProject() |
|                15.傅里叶变换                |    学习如何通过OpenCV进行傅里叶变换、获得振幅谱、高通滤波    | np.fft.fft2()<br />np.fft.fftshift()<br />cv2.dft()<br />cv2.idft()<br />cv2.magnitude() |
|                16.还在更新中                |                                                              |                                                              |
|                                             |                                                              |                                                              |
