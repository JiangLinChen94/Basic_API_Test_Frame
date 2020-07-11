#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 19:35
import requests
import unittest
from common.local_config_utils import local_config
from common.log_utils import logger
from common import common_api
from common import common_action


class GetTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_get_tag(self):
        self._testMethodDoc = '[Test_VXAPI_007]验证获取标签接口能否成功执行'
        logger.info('[Test_VXAPI_007] 验证获取标签接口能否成功执行')
        access_token_value = common_action.get_access_token_value(self.session)
        get_tag_response = common_api.get_user_tag_api(self.session, access_token_value)
        actual_result = get_tag_response.json()['tags'][0]['name']
        self.assertEqual(actual_result, '星标组')


if __name__ == '__main__':
    unittest.main()
