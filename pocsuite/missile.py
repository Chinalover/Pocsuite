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
    def __init__(self, target, missile_info={}):

        if missile_info['db']:
            import known
            missile_info[ids] = read_db(id)
        else:
            missile_info[ids] = id2path()


        PCS_OPTIONS.update({
            'url': target,
            'pocFile': missile_info['ids'],
            'headers': headers,
            'extra_params': params,
            'Mode': missile_info['mode']
        })

    def run(self):
        result = pcsInit(PCS_OPTIONS)
        return result[0]


if __name__ == '__main__':
    missile_info = {
        'mode': 'verify',  # 默认为verify，可以不包含该字段
        'ids': 'tests/poc_example1.py',  # 默认为空，可以不包含该字段
        'db': 
    }
    target = 'baidu.com'

    mis = Missile(target, missile_info)
    res = mis.run()
    print res
    print res[-1].result
