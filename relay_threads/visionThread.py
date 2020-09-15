# -*- encoding: UTF-8 -*-
"""
机器人视觉线程
"""
import random
from threading import Thread
from naoqi import ALProxy
import cv2
import numpy as np


class VisionThread(Thread):
    def __init__(self, robot_conf, start_vision_queue, vision_move_queue):
        super(VisionThread, self).__init__()

        self.__robot_conf = robot_conf
        self.__start_vision_queue = start_vision_queue
        self.__vision_move_queue = vision_move_queue

        self.__vision = ALProxy("ALVideoDevice",
                                self.__robot_conf['basic']['param']['ip'],
                                self.__robot_conf['basic']['param']['port'])

        self.camera_botton = None  # 底部摄像头订阅
        self.init_camera()

    def init_camera(self):
        # 摄像头参数
        cameraName = 'camera' + str(random.randint(0, 100))
        cameraIndex = 1
        resolution = 1
        colorSpace = 13
        fps = 30

        self.camera_botton = self.__vision.subscribeCamera(cameraName,
                                                           cameraIndex,
                                                           resolution,
                                                           colorSpace,
                                                           fps)

    def image_houghlines(self, img):
        # 转换成numpy数组
        image = np.frombuffer(img[6], dtype=np.uint8)
        # 切割
        image = image.reshape(img[1], img[0], img[2])
        # HSV
        grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # 二值化
        # H, S, V = cv2.split(grayimg)
        lowerGreen = np.array([0, 0, 150])
        upperGreen = np.array([120, 17, 255])
        mask = cv2.inRange(grayimg, lowerGreen, upperGreen)
        greenThings = cv2.bitwise_and(image, image, mask=mask)
        # 二值化
        img = cv2.GaussianBlur(greenThings, (3, 3), 0)
        imcan = cv2.Canny(img, 50, 150, apertureSize=3)
        # 检测霍夫线
        lines = cv2.HoughLinesP(imcan, 1, np.pi / 180, 50, minLineLength=200, maxLineGap=10)
        return lines

    def direction_recognition(self, lines):
        print len(lines)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            print line
            slope = abs((y1 - y2) / (x1 - x2))
            print "slope:", slope
            theta = np.arctan(slope)
            print '弧度制单位：', theta
            print '角度制单位：', np.degrees(theta)

    def run(self):
        # while True:
        #     if not self.__start_vision_queue.empty():
        #         msg = self.__start_vision_queue.get()
        #         if msg == 'start':
        #             break

        while True:
            image = self.__vision.getImageRemote(self.camera_botton)
            # todo
            lines = self.image_houghlines(image)
            cmd = self.direction_recognition(lines)

            break
            # 判断停止后，断开摄像头订阅
            # self.__vision.unsubscribeCamera(self.camera_botton)


if __name__ == '__main__':
    from conf import robot1_conf
    from Queue import Queue

    queue1 = Queue()
    queue2 = Queue()
    vision = VisionThread(robot1_conf, queue1, queue2)
    vision.start()
    vision.join()