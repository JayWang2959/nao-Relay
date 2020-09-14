# -*- encoding: UTF-8 -*-
"""
机器人视觉线程
"""
from threading import Thread


class VisionThread(Thread):
    def __init__(self, robot_conf, start_vision_queue, vision_move_queue):
        super(VisionThread, self).__init__()

        self.__robot_conf = robot_conf
        self.__start_vision_queue = start_vision_queue
        self.__vision_move_queue = vision_move_queue

    def run(self):
        while True:
            if not self.__start_vision_queue.empty():
                msg = self.__start_vision_queue.get()
                if msg == 'start':
                    break
