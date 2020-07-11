#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 16:34

import requests
import unittest
from common.local_config_utils import local_config
from common.log_utils import logger
from common import common_api


class GetAccessTokenCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        self._testMethodDoc = '[Test_VXAPI_001]验证获取access_token接口能否正常执行'
        logger.info('[Test_VXAPI_001] 验证获取access_token接口能否正常执行')
        get_access_token_response = common_api.get_access_token_api(self.session,
                                                                    'client_credential',
                                                                    'wxec83eaada223a9c8',
                                                                    '1867d7f1cabb3bafae0b7304e8251a09')
        actual_result = get_access_token_response.json()['expires_in']
        self.assertEqual(actual_result, 7200)

    def test_get_access_token_appid_error(self):
        self._testMethodDoc = '[Test_VXAPI_002] 验证获取access_token接口appid错误'
        logger.info('[Test_VXAPI_002] 验证获取access_token接口appid错误')
        get_access_token_response = common_api.get_access_token_api(self.session,
                                                                    'client_credential',
                                                                    'wxec83eaada223',
                                                                    '1867d7f1cabb3bafae0b7304e8251a09')
        actual_result = get_access_token_response.json()['errcode']
        self.assertEqual(actual_result, 40013)

    def test_get_access_token_secret_error(self):
        self._testMethodDoc = '[Test_VXAPI_002] 验证获取access_token接口secret错误'
        logger.info('[Test_VXAPI_002] 验证获取access_token接口secret错误')
        get_access_token_response = common_api.get_access_token_api(self.session,
                                                                    'client_credential',
                                                                    'wxec83eaada223a9c8',
                                                                    '1867d7f1cabb3bafae0b7304e8')
        actual_result = get_access_token_response.json()['errcode']
        self.assertEqual(actual_result, 40125)


if __name__ == '__main__':
    unittest.main()
