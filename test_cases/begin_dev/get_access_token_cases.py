#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 16:34

import requests
import unittest
from common.local_config_utils import local_config
from common.log_utils import logger


class GetAccessTokenCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        self._testMethodDoc = '[case1]成功获取access_token值'
        logger.info('[case01] 正常获取access_token值测试')
        params = {
            'grant_type': 'client_credential',
            'appid': 'wxec83eaada223a9c8',
            "secret": "1867d7f1cabb3bafae0b7304e8251a09"
        }
        get_access_token_response = self.session.get(url=self.hosts + '/cgi-bin/token',
                                                     params=params)
        actual_result = get_access_token_response.json()['expires_in']
        self.assertEqual(actual_result, 7200)

    def test_get_access_token_appid_error(self):
        self._testMethodDoc = '[case2]appid错误'
        self._testMethodDoc = '[case02] appid错误时测试'
        params = {
            'grant_type': 'client_credential',
            'appid': 'wxec83eaada223a',
            "secret": "1867d7f1cabb3bafae0b7304e8251a09"
        }
        get_access_token_response = self.session.get(url=self.hosts + '/cgi-bin/token',
                                                     params=params)
        actual_result = get_access_token_response.json()['errcode']
        self.assertEqual(actual_result, 40013)


if __name__ == '__main__':
    unittest.main()
