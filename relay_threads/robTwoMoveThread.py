# -*- encoding: UTF-8 -*-
"""
机器人2号的运动线程
"""
from relay_threads import MoveThread


class RobTwoMoveThread(MoveThread):
    def __init__(self, robot_conf, start_move_queue, vision_move_queue):
        super(self.__class__, self).__init__(robot_conf, start_move_queue, vision_move_queue)

    def run(self):
        self.wait_to_start()
        self.move()
        # todo 完成任务的反馈


