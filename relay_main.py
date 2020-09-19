# -*- encoding: UTF-8 -*-
"""
程序入口
"""

from Queue import Queue
# from naoqi import ALProxy

from conf import robot1_conf
from conf import robot2_conf

from relay_threads import RobOneStartThread
from relay_threads import RobOneMoveThread
# from relay_threads import RobTwoStartThread
# from relay_threads import RobTwoMoveThread
from relay_threads import VisionThread


def main():

    r1_start_move_queue = Queue(maxsize=1000)
    r1_start_vision_queue = Queue(maxsize=1000)
    r1_vision_move_queue = Queue(maxsize=1000)

    r2_start_move_queue = Queue(maxsize=1000)
    r2_start_vision_queue = Queue(maxsize=1000)
    r2_vision_move_queue = Queue(maxsize=1000)

    # 1号机器人等待出发线程
    r1start = RobOneStartThread(robot1_conf, r1_start_move_queue, r1_start_vision_queue)
    r1start.start()
    # 1号机器人运动线程
    r1motion = RobOneMoveThread(robot1_conf, r1_start_move_queue, r1_vision_move_queue)
    r1motion.start()
    # 1号机器人视觉线程
    r1vision = VisionThread(robot1_conf, r1_start_vision_queue, r1_vision_move_queue)
    r1vision.start()

    # # 2号机器人等待出发线程
    # r2start = RobTwoStartThread(robot2_conf, r2_start_move_queue, r2_start_vision_queue)
    # r2start.start()
    # # 2号机器人运动线程
    # r2motion = RobTwoMoveThread(robot2_conf, r2_start_move_queue, r2_vision_move_queue)
    # r2motion.start()
    # # 2号机器人视觉线程
    # r2vision = VisionThread(robot2_conf, r2_start_vision_queue, r2_vision_move_queue)
    # r2vision.start()

    # wait for join
    # r2vision.join()
    # r2motion.join()
    # r2start.join()
    r1vision.join()
    r1motion.join()
    r1start.join()


if __name__ == "__main__":
    main()
