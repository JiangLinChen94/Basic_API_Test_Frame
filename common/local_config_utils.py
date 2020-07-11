#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 11:04

import os
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '..', r'config/config.ini')


class LocalConfigUtils():
    def __init__(self, config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path, encoding='utf-8')

    @property  # 把方法变为属性方法
    def URL(self):
        url_value = self.cfg.get('default', 'URL')
        return url_value

    @property
    def LOG_PATH(self):
        log_path = self.cfg.get('path', 'LOG_PATH')
        return log_path

    @property
    def LOG_LEVEL(self):
        log_level = int(self.cfg.get('log', 'LOG_LEVEL'))
        return log_level

    @property
    def REPORT_PATH(self):
        report_path = self.cfg.get('path', 'REPORT_PATH')
        return report_path


local_config = LocalConfigUtils()

if __name__ == '__main__':
    cfg = LocalConfigUtils()
    print(cfg.URL)
    print(cfg.LOG_PATH)
    # print(cfg.REPORT_PATH)
