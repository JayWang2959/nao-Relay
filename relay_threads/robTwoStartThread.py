# -*- encoding: UTF-8 -*-
"""
2号机器人等待出发的线程，等待1号机器人的信号
"""

from threading import Thread
from naoqi import ALProxy
import socket
import qi
import time


class RobTwoStartThread(Thread):
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
            HOST = '127.0.0.1'  # Symbolic name meaning all available interfaces
            PORT = 50007  # Arbitrary non-privileged port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((HOST, PORT))
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
