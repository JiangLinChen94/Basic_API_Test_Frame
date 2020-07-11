#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 19:00

from common.local_config_utils import local_config
from common import common_api


def get_access_token_value(session):
    get_access_token_response = common_api.get_access_token_api(session,
                                                                'client_credential',
                                                                'wxec83eaada223a9c8',
                                                                '1867d7f1cabb3bafae0b7304e8251a09')
    access_token_value = get_access_token_response.json()['access_token']
    return access_token_value
