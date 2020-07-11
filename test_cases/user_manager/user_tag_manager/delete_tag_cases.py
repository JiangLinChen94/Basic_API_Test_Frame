#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 20:00

import requests
import unittest
from common.local_config_utils import local_config
from common.log_utils import logger
from common import common_api
from common import common_action


class DeleteTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_delete_tag(self):
        self._testMethodDoc = '[Test_VXAPI_010]验证删除标签接口能否成功执行'
        logger.info('[Test_VXAPI_010] 验证删除标签接口能否成功执行')
        access_token_value = common_action.get_access_token_value(self.session)
        json_data = {"tag": {"id": 103}}
        update_tag_response = common_api.delete_user_tag_api(self.session, access_token_value, json_data)
        actual_result = update_tag_response.json()['errmsg']
        self.assertEqual(actual_result, 'ok')

    def test_delete_default_tag_id(self):
        self._testMethodDoc = '[Test_VXAPI_011]验证删除标签接口能否成功执行'
        logger.info('[Test_VXAPI_011] 验证删除标签接口能否成功执行')
        access_token_value = common_action.get_access_token_value(self.session)
        json_data = {"tag": {"id": 2}}
        update_tag_response = common_api.delete_user_tag_api(self.session, access_token_value, json_data)
        actual_result = update_tag_response.json()['errcode']
        print(actual_result)
        self.assertEqual(actual_result, 45058)


if __name__ == '__main__':
    unittest.main()
