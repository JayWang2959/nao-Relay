# -*- encoding: UTF-8 -*-
"""
2号机器人等待出发的线程，等待1号机器人的信号
"""

from threading import Thread
from naoqi import ALProxy
import socket


class RobTwoStartThread(Thread):
    def __init__(self, robot_conf, start_move_queue, start_vision_queue):
        super(RobTwoStartThread, self).__init__()

        self.__robot_conf = robot_conf
        self.__start_move_queue = start_move_queue
        self.__start_vision_queue = start_vision_queue

        # self.__Audio = ALProxy("ALTextToSpeech",
        #                        self.__robot_conf['basic_param']['ip'],
        #                        self.__robot_conf['basic_param']['port'])
        #

    def run(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.__robot_conf['tcp']['host'],
                    self.__robot_conf['tcp']['port']))
            s.listen(1)
            conn, addr = s.accept()
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
            conn.close()
            self.__start_move_queue.put('start')
            self.__start_vision_queue.put('start')
            break
        print 'rob 2 received message'


# if __name__ == '__main__':
#     from conf import robot1_conf
#     from Queue import Queue
#     queue1 = Queue()
#     queue2 = Queue()
#
#     rob2start = RobTwoStartThread(robot1_conf, queue1, queue2)
#     rob2start.start()
#     rob2start.join()
