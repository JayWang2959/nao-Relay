# -*- encoding: UTF-8 -*-
"""
机器人视觉线程
"""
import random
from threading import Thread
from naoqi import ALProxy
import cv2


class VisionThread(Thread):
    def __init__(self, robot_conf, start_vision_queue, vision_move_queue):
        super(VisionThread, self).__init__()

        self.__robot_conf = robot_conf
        self.__start_vision_queue = start_vision_queue
        self.__vision_move_queue = vision_move_queue

        self.__vision = ALProxy("ALVideoDevice",
                                self.__robot_conf['basic']['param']['ip'],
                                self.__robot_conf['basic']['param']['port'])

        self.camera_botton = None                 # 底部摄像头订阅
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

    def run(self):
        while True:
            if not self.__start_vision_queue.empty():
                msg = self.__start_vision_queue.get()
                if msg == 'start':
                    break

        while True:
            image = self.__vision.getImageRemote(self.camera_botton)
            # todo

            # 判断停止后，断开摄像头订阅
            self.__vision.unsubscribeCamera(self.camera_botton)