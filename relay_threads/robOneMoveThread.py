# -*- encoding: UTF-8 -*-
"""
机器人1号的运动线程
"""
from relay_threads import MoveThread


class RobOneMoveThread(MoveThread):
    def __init__(self, robot_conf, start_move_queue, vision_move_queue):
        super(self.__class__, self).__init__(robot_conf, start_move_queue, vision_move_queue)

    def run(self):
        self.wait_to_start()
        self.move()
        # todo 发送tcp给2号机器人


# if __name__ == '__main__':
#     from conf import robot1_conf
#     from Queue import Queue
#     queue1 = Queue()
#     queue2 = Queue()
#
#     robonemove = RobOneMoveThread(robot1_conf, queue1, queue2)
