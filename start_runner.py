#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 16:57

import unittest
from common import HTMLTestReportCN
from common.local_config_utils import local_config


def get_all_cases_suite():
    discover = unittest.defaultTestLoader.discover(
        start_dir='./test_cases',
        pattern='*_cases.py',
        top_level_dir='./test_cases'
    )
    all_cases_suite = unittest.TestSuite()
    all_cases_suite.addTest(discover)
    return all_cases_suite


report_dir = HTMLTestReportCN.ReportDirectory(local_config.REPORT_PATH + '/')
report_dir.create_dir('API_TEST_')
# dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
fp = open(report_path, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         tester="newdream",
                                         title="newdream_API_TEST",
                                         description="study~~~")
runner.run(get_all_cases_suite())
fp.close()
