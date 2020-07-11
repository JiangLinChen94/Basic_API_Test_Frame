#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 18:26

from common.local_config_utils import local_config


def get_access_token_api(session, grant_type, appid, secret):
    params = {
        'grant_type': grant_type,
        'appid': appid,
        "secret": secret
    }
    response = session.get(url=local_config.URL + '/cgi-bin/token',
                           params=params)
    return response


def create_user_tag_api(session, access_token, tag_json):
    params = {
        'access_token': access_token
    }
    json_data = tag_json
    response = session.post(url=local_config.URL + '/cgi-bin/tags/create',
                            params=params,
                            json=json_data)
    return response


def get_user_tag_api(session, access_token):
    params = {
        'access_token': access_token
    }
    response = session.get(url=local_config.URL + '/cgi-bin/tags/get',
                           params=params)
    return response


def update_user_tag_api(session, access_token, tag_info):
    params = {
        'access_token': access_token
    }
    tag_info = tag_info
    response = session.post(url=local_config.URL + '/cgi-bin/tags/update',
                            params=params,
                            json=tag_info)
    return response


def delete_user_tag_api(session, access_token, tagid_json):
    params = {
        'access_token': access_token,
    }
    json_data = tagid_json
    response = session.post(url=local_config.URL + '/cgi-bin/tags/delete',
                            params=params,
                            json=json_data)
    return response


def update_remark_user_tag_api(session, access_token, tag_info_json):
    params = {
        'access_token': access_token,
    }
    json_data = tag_info_json
    response = session.post(url=local_config.URL + '/cgi-bin/user/info/updateremark',
                            params=params,
                            json=json_data)
    return response
