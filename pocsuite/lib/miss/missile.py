#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Copyright
"""

import sys
from pocsuite import pcsInit
from lib.core.settings import PCS_OPTIONS
from lib.core.common import banner


class Missile():
    def __init__(self, target, missile_info={}, headers={}, params={}):
        PCS_OPTIONS.update({
            'url': target,
            'pocFile': missile_info['ids'],
            'headers': headers,
            'extra_params': params,
            'Mode': missile_info['mode']
        })

    def run(self):
        result = pcsInit(PCS_OPTIONS)
        return result


if __name__ == '__main__':
    missile_info = {
        'mode': 'verify',  # 默认为verify，可以不包含该字段
        'ids': 'tests/poc_example1.py'  # 默认为空，可以不包含该字段
    }
    target = 'baidu.com'

    mis = Missile(target, missile_info)
    result = mis.run()
    print result[-1]
