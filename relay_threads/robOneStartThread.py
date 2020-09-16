# -*- encoding: UTF-8 -*-
"""
1号机器人等待出发的线程
"""
from threading import Thread
from naoqi import ALProxy
import time


class RobOneStartThread(Thread):
    def __init__(self, robot_conf, start_move_queue, start_vision_queue):
        super(self.__class__, self).__init__()

        self.__robot_conf = robot_conf
        self.__start_move_queue = start_move_queue
        self.__start_vision_queue = start_vision_queue

        self.__Audio = ALProxy("ALAudioDevice",
                               self.__robot_conf['basic_param']['ip'],
                               self.__robot_conf['basic_param']['port'])

    def run(self):
        while True:
            sp = self.__Audio.getRightMicEnergy()  # 打开麦克风
            time.sleep(0.5)
            if sp > 20000:
                sp = 0
                self.__start_move_queue.put('start')
                self.__start_vision_queue.put('start')
            break



