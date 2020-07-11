#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 20:11

import requests
import unittest
from common.local_config_utils import local_config
from common.log_utils import logger
from common import common_api
from common import common_action


class UpdateRemarkTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_update_remark(self):
        self._testMethodDoc = '[Test_VXAPI_012]验证设置用户备注名能否成功执行'
        logger.info('[Test_VXAPI_012] 验证设置用户备注名能否成功执行')
        access_token_value = common_action.get_access_token_value(self.session)
        json_data = {"openid": "od-53v0GMqGTEiPY-QC549RTXkCk", "remark": "pangzi"}
        create_tag_response = common_api.update_remark_user_tag_api(self.session, access_token_value, json_data)
        actual_result = create_tag_response.json()['errmsg']
        self.assertEqual(actual_result, 'ok')

    def test_update_remark_openid_error(self):
        self._testMethodDoc = '[Test_VXAPI_013]验证openid错误设置用户备注名能否成功执行'
        logger.info('[Test_VXAPI_013] 验证openid错误设置用户备注名能否成功执行')
        access_token_value = common_action.get_access_token_value(self.session)
        json_data = {"openid": "od-53v0GMqGTEiPY-QC549R", "remark": "pangzi"}
        create_tag_response = common_api.update_remark_user_tag_api(self.session, access_token_value, json_data)
        actual_result = create_tag_response.json()['errcode']
        self.assertEqual(actual_result, 40003)


if __name__ == '__main__':
    unittest.main()
