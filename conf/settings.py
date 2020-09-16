# -*- encoding: UTF-8 -*-
"""
配置文件 机器人ip、运动参数等都写在这里
"""

robot1_conf = {                                         # 1号机器人参数
    'basic_param': {                                    # 基础参数
        'ip': '192.168.43.250',
        'port': 9559,
    },
    'motion_param': {                                   # 运动参数
        'forward': {                                    # 前进
            'x': 1,
            'y': 0,
            'theta': 0,
            'config': [
                ["MaxStepFrequency", 0.2],
                ["MaxStepTheta", 0.0005],
                ["MaxStepX", 0.02],
                ["MaxStepY", 0.101],
                ["StepHeight", 0.005],
                ["TorsoWx", 0],
                ["TorsoWy", 0]
            ]
        },
        'left': {                                       # 左转
            'x': 0,
            'y': 0,
            'theta': 0.5,
            'config': [
                ["MaxStepFrequency", 0.2],
                ["MaxStepTheta", 0.0005],
                ["MaxStepX", 0.02],
                ["MaxStepY", 0.101],
                ["StepHeight", 0.005],
                ["TorsoWx", 0],
                ["TorsoWy", 0]
            ]
        },
        'right': {                                      # 右转
            'x': 0,
            'y': 0,
            'theta': -0.5,
            'config': [
                ["MaxStepFrequency", 0.2],
                ["MaxStepTheta", 0.0005],
                ["MaxStepX", 0.02],
                ["MaxStepY", 0.101],
                ["StepHeight", 0.005],
                ["TorsoWx", 0],
                ["TorsoWy", 0]
            ]
        }
    }
}

robot2_conf = {                                         # 2号机器人参数
    'basic_param': {                                    # 基础参数
        'ip': '192.168.43.250',
        'port': 9559,
    },
    'motion_param': {  # todo 运动参数待添加

    }
}
