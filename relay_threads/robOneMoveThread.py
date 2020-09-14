# -*- encoding: UTF-8 -*-
"""
机器人1号的运动线程
"""
from threading import Thread
from naoqi import ALProxy


class RobOneMoveThread(Thread):
    def __init__(self, robot_conf, start_move_queue, vision_move_queue):
        super(self.__class__, self).__init__()

        self.__robot_conf = robot_conf
        self.__start_move_queue = start_move_queue
        self.__vision_move_queue = vision_move_queue

        # self.__memory = ALProxy('ALMemory',
        #                         robot_conf['basic_param']['ip'],
        #                         robot_conf['basic_param']['port'])

        self.__motion = ALProxy("ALMotion",
                                self.__robot_conf['basic_param']['ip'],
                                self.__robot_conf['basic_param']['port'])

    def run(self):
        # 等待开始线程发来出发指令
        while True:
            if not self.__start_move_queue.empty():
                msg = self.__start_move_queue.get()
                if msg == 'start':
                    break

        while True:
            if not self.__vision_move_queue.empty():
                msg = self.__vision_move_queue.get()
                if msg == 'left':  # 左转
                    pass
                if msg == 'right':  # 右转
                    pass
                if msg == 'forward':  # 直行
                    pass
                if msg == 'stop':  # 停
                    pass
