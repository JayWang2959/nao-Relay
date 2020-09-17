# -*- encoding: UTF-8 -*-
"""
1号机器人等待出发的线程
"""
from threading import Thread
from naoqi import ALProxy


class RobOneStartThread(Thread):
    def __init__(self, robot_conf, start_move_queue, start_vision_queue):
        super(RobOneStartThread, self).__init__()

        self.__robot_conf = robot_conf
        self.__start_move_queue = start_move_queue
        self.__start_vision_queue = start_vision_queue

        self.__touch = ALProxy("ALTouch",
                               self.__robot_conf['basic_param']['ip'],
                               self.__robot_conf['basic_param']['port'])

    def run(self):
        while True:
            status = self.__touch.getStatus()
            for e in status:
                if e[0] == 'Head' and e[1]:
                    self.__start_move_queue.put('start')
                    self.__start_vision_queue.put('start')
                    break

