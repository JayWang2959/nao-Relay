# -*- encoding: UTF-8 -*-
"""
机器人1号的运动线程
"""
import socket
from relay_threads import MoveThread


class RobOneMoveThread(MoveThread):
    def __init__(self, robot_conf, start_move_queue, vision_move_queue):
        super(RobOneMoveThread, self).__init__(robot_conf, start_move_queue, vision_move_queue)
        self.__robot_conf = robot_conf

    def sendTcp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.__robot_conf['tcp']['host'],
                   self.__robot_conf['tcp']['port']))
        s.sendall(b'Hello, world')
        s.recv(1024)
        s.close()

    def run(self):
        self.wait_to_start()
        self.move()
        # self.sendTcp()


# if __name__ == '__main__':
#     from conf import robot1_conf
#     from Queue import Queue
#     queue1 = Queue()
#     queue2 = Queue()
#
#     robonemove = RobOneMoveThread(robot1_conf, queue1, queue2)
