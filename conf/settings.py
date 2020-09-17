# -*- encoding: UTF-8 -*-
"""
配置文件 机器人ip、运动参数等都写在这里
"""

robot1_conf = {                                         # 1号机器人参数
    'basic_param': {                                    # 基础参数
        'ip': '172.20.10.8',
        'port': 9559,
    },
    'motion_param': {                                   # 运动参数
        'forward': {                                    # 前进
            'x': 1,
            'y': 0,
            'theta': 0,
            'config': [
                ["MaxStepFrequency", 0.8],
                ["MaxStepTheta", 0.4],
                ["MaxStepX", 0.05],
                ["MaxStepY", 0.2],
                ["StepHeight", 0.01],
                ["TorsoWx", 0],
                ["TorsoWy", 0]
            ]
        },
        'left': {                                       # 左转
            'x': 0.8,
            'y': 0,
            'theta': 0.05,
            'config': [
                ["MaxStepFrequency", 0.8],
                ["MaxStepTheta", 0.4],
                ["MaxStepX", 0.05],
                ["MaxStepY", 0.2],
                ["StepHeight", 0.01],
                ["TorsoWx", 0],
                ["TorsoWy", 0]
            ]
        },
        'right': {                                      # 右转
            'x': 0.8,
            'y': 0,
            'theta': -0.1,
            'config': [
                ["MaxStepFrequency", 0.8],
                ["MaxStepTheta", 0.4],
                ["MaxStepX", 0.05],
                ["MaxStepY", 0.2],
                ["StepHeight", 0.01],
                ["TorsoWx", 0],
                ["TorsoWy", 0]
            ]
        }
    },
    'tcp': {
        'host': '127.0.0.1',
        'port': 50007
    }
}

robot2_conf = {                                         # 2号机器人参数
    'basic_param': {                                    # 基础参数
        'ip': '192.168.43.250',
        'port': 9559,
    },
    'motion_param': {  # todo 运动参数待添加

    },
    'tcp': {
        'host': '127.0.0.1',
        'port': 50007
    }
}
