# -*- encoding: UTF-8 -*-
"""
程序入口
"""

from Queue import Queue
from naoqi import ALProxy

from conf import robot1_conf
from conf import robot2_conf

from relay_threads import RobOneMoveThread
from relay_threads import RobOneStartThread
from relay_threads import VisionThread


def main():

    r1_start_move_queue = Queue(maxsize=1000)
    r1_start_vision_queue = Queue(maxsize=1000)
    r1_vision_move_queue = Queue(maxsize=1000)

    r2_start_move_queue = Queue(maxsize=1000)
    r2_start_vision_queue = Queue(maxsize=1000)
    r2_vision_move_queue = Queue(maxsize=1000)

    # 1号机器人等待出发线程
    r1start = RobOneStartThread(robot1_conf, r1_start_move_queue)
    r1start.start()
    # 1号机器人运动线程
    r1motion = RobOneMoveThread(robot1_conf, r1_start_move_queue, r1_vision_move_queue)
    r1motion.start()
    # 1号机器人视觉线程
    r1vision = VisionThread(robot1_conf, r1_start_vision_queue, r1_vision_move_queue)
    r1vision.start()
    # todo 2号机器人等待出发线程
    # todo 2号机器人运动线程
    # todo 2号机器人视觉线程

    # wait for join
    r1vision.join()
    r1motion.join()
    r1start.join()


if __name__ == "__main__":
    main()
