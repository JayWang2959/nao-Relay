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


def main():

    r1_start_move_queue = Queue(maxsize=1000)
    r1_start_vision_queue = Queue(maxsize=1000)
    r1_vision_move_queue = Queue(maxsize=1000)

    r2_start_move_queue = Queue(maxsize=1000)
    r2_start_vision_queue = Queue(maxsize=1000)
    r2_vision_move_queue = Queue(maxsize=1000)

    motion = RobOneMoveThread(robot1_conf, r1_start_move_queue, r1_vision_move_queue)
    r1start = RobOneStartThread(robot1_conf, r1_start_move_queue)

    motion.start()
    r1start.start()

    r1start.join()
    motion.join()


if __name__ == "__main__":
    main()
