#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Copyright (c) 2014-2015 pocsuite developers (http://sebug.net)
See the file 'docs/COPYING' for copying permission
"""

# import sys; sys.path.append('Pocsuite/pocsuite') 将pocsuite.py路径添加到sys.path
# 运行时需要在调用Missile的目录创建modules/tmp/文件夹
from pocsuite import pcsInit
from lib.core.settings import PCS_OPTIONS
from lib.core.common import banner


class Missile():
    def __init__(self, target, missile_info={}):

        if missile_info['db']:
            # from knwonledge import read_db
            with open('modules/ssv_%s.py' % missile_info['ids'], 'a') \
                    as fp:
                fp.write(self.read_db(id))
            missile_info['ids'] = 'modules/ssv_%s.py' % missile_info['ids']

        PCS_OPTIONS.update({
            'url': target,
            'pocFile': missile_info['ids'],
            'headers': missile_info['headers'],
            'extra_params': missile_info['params'],
            'Mode': missile_info['mode']
        })

    def run(self):
        result = pcsInit(PCS_OPTIONS)
        return result[0]

    def id2path():
        pass

    def read_db(self, t):
        with open('Pocsuite/pocsuite/tests/poc_example1.py') as fp:
            content = fp.read()
        return content



if __name__ == '__main__':
    missile_info = {
        'mode': 'verify',  # 默认为verify，可以不包含该字段
        'ids': '123',  # 默认为空，可以不包含该字段
        'headers': None,
        'params': None,
        'db':  '123'
    }
    target = 'baidu.com'

    mis = Missile(target, missile_info)
    res = mis.run()
    print res
    print res[-1].result
"""
import sys; sys.path.append('Pocsuite/pocsuite');from missile import Missile
"""
