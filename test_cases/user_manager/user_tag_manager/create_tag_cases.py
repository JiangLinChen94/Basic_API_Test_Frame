#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 19:06
import requests
import unittest
from common.local_config_utils import local_config
from common.log_utils import logger
from common import common_api
from common import common_action


class CreateTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_add_tag(self):
        self._testMethodDoc = '[Test_VXAPI_004]验证创建标签接口能否成功执行'
        logger.info('[Test_VXAPI_004] 验证创建标签接口能否成功执行')
        access_token_value = common_action.get_access_token_value(self.session)
        json_data = {"tag": {"name": "xiaowangshu102"}}
        create_tag_response = common_api.create_user_tag_api(self.session, access_token_value, json_data)
        actual_result = create_tag_response.json()['tag']['name']
        self.assertEqual(actual_result, 'xiaowangshu102')

    def test_tag_name_redo(self):
        self._testMethodDoc = '[Test_VXAPI_005]验证创建标签接口重复标签名创建'
        logger.info('[Test_VXAPI_005] 验证创建标签接口重复标签名创建')
        access_token_value = common_action.get_access_token_value(self.session)
        json_data = {"tag": {"name": "xiaowangshu"}}
        create_tag_response = common_api.create_user_tag_api(self.session, access_token_value, json_data)
        actual_result = create_tag_response.json()['errcode']
        self.assertEqual(actual_result, 45157)

    def test_tag_name_long(self):
        self._testMethodDoc = '[Test_VXAPI_006]验证创建标签接口标签名超过30个字符'
        logger.info('[Test_VXAPI_006] 验证创建标签接口标签名超过30个字符')
        access_token_value = common_action.get_access_token_value(self.session)
        json_data = {"tag": {"name": "xiaowangshuasdfasldkfjlaskasdfjdflkasjdflkjsadlfjlaksdfaskldfjalksdfj"}}
        create_tag_response = common_api.create_user_tag_api(self.session, access_token_value, json_data)
        actual_result = create_tag_response.json()['errcode']
        self.assertEqual(actual_result, 45158)


if __name__ == '__main__':
    unittest.main()
