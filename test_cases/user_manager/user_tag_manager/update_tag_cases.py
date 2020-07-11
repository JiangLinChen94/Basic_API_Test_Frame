#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 19:44

import requests
import unittest
from common.local_config_utils import local_config
from common.log_utils import logger
from common import common_api
from common import common_action


class UpdateTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_update_tag_name(self):
        self._testMethodDoc = '[Test_VXAPI_008]验证编辑标签接口能否成功执行'
        logger.info('[Test_VXAPI_008] 验证编辑标签接口能否成功执行')
        access_token_value = common_action.get_access_token_value(self.session)
        json_data = {"tag": {"id": 134, "name": "Senbonzakura003"}}
        update_tag_response = common_api.update_user_tag_api(self.session, access_token_value, json_data)
        actual_result = update_tag_response.json()['errmsg']
        self.assertEqual(actual_result, 'ok')

    def test_update_tag_name_redo(self):
        self._testMethodDoc = '[Test_VXAPI_009]验证编辑标签接口名称重复能否执行成功'
        logger.info('[Test_VXAPI_009] 验证编辑标签接口名称重复能否执行成功')
        access_token_value = common_action.get_access_token_value(self.session)
        json_data = {"tag": {"id": 136, "name": "Alin"}}
        update_tag_response = common_api.update_user_tag_api(self.session, access_token_value, json_data)
        actual_result = update_tag_response.json()['errcode']
        print(update_tag_response.json())
        self.assertEqual(actual_result, 45157)


if __name__ == '__main__':
    unittest.main()
