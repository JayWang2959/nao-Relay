# -*- encoding: UTF-8 -*-
"""
机器人2号的运动线程
"""
# todo 整合1、2号机器人的运动线程类，提取公共模块作父类继承

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

        self.__posture = ALProxy("ALPosture",
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
            # wake up robot
            self.__motion.wakeup()
            self.__posture.goToPosture("StandInit", 0.5)

            if not self.__vision_move_queue.empty():
                msg = self.__vision_move_queue.get()
                if msg == 'left':           # 左转
                    self.__motion.moveTo(self.__robot_conf['motion_param']['left']['x'],
                                         self.__robot_conf['motion_param']['left']['y'],
                                         self.__robot_conf['motion_param']['left']['theta'],
                                         self.__robot_conf['motion_param']['left']['config'])
                if msg == 'right':          # 右转
                    self.__motion.moveTo(self.__robot_conf['motion_param']['right']['x'],
                                         self.__robot_conf['motion_param']['right']['y'],
                                         self.__robot_conf['motion_param']['right']['theta'],
                                         self.__robot_conf['motion_param']['right']['config'])
                if msg == 'forward':        # 直行
                    self.__motion.moveTo(self.__robot_conf['motion_param']['forward']['x'],
                                         self.__robot_conf['motion_param']['forward']['y'],
                                         self.__robot_conf['motion_param']['forward']['theta'],
                                         self.__robot_conf['motion_param']['forward']['config'])
                if msg == 'stop':           # 停
                    # todo 可以做一些完成的姿势
                    self.__motion.stopMove()
                    self.__motion.rest()
                    break
