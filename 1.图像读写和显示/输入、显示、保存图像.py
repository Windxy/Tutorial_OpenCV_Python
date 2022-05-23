import cv2 #引用模块


if __name__ == '__main__':
    # 1.输入图像
    img = cv2.imread('img/tiger.jpg', 1)

    # 2.显示图像
    cv2.namedWindow('img_win',cv2.WINDOW_NORMAL)  # WINDOW_NORMAL/WINDOW_FREERATIO/WINDOW_GUI_NORMAL
    cv2.imshow('img_win',img)
    k = cv2.waitKey(0)
    if k==27:                    #对应键盘上的ESC按键
       cv2.destroyAllWindows()   #销毁所有窗口
    elif k==ord('s') :           #按下s，保存图像
        cv2.imwrite('img/tiger.jpg', img)    # 3.保存图像
        cv2.destroyAllWindows()
