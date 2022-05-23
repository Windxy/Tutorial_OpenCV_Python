import cv2

'''从摄像头读取图像'''
def CapFromCamera():
    cap = cv2.VideoCapture(0)

    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 获取宽高帧数
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    while(True):
        ret, frame = cap.read()                        #读取帧
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):          #按‘q’退出
            break

    #释放资源并关闭窗口
    cap.release()
    cv2.destroyAllWindows()

'''从视频中读取图像'''
def CapFromVedio():
    cap = cv2.VideoCapture('img/Guanggao1.mp4')

    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 获取宽高帧数
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)

        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    CapFromCamera()