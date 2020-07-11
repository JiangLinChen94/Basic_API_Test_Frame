#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 17:42

import re
import requests

# 注册页面
session = requests.session()

register_page_header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}

register_page_param = {
    "m": "u",
    "c": "register"
}
register_page_response = session.get('http://47.107.178.45/phpwind/index.php',
                                     params=register_page_param,
                                     headers=register_page_header)
register_page_body = register_page_response.content.decode('utf-8')
csrf_token_value = re.findall('name="csrf_token" value="(.+?)"/>', register_page_body)[0]

# 申请注册url
register_apply_url = 'http://47.107.178.45/phpwind/index.php'
# 申请注册请求头
register_apply_header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
# 申请注册参数
register_apply_param = {
    "m": "u",
    "c": "register",
    "a": "dorun",
}

register_apply_data = {
    "username": "cjl20200712",
    "password": "123456",
    "repassword": "123456",
    "email": "cjl20200712@aliyun.com",
    "csrf_token": csrf_token_value
}

register_apply_response = session.post(url=register_apply_url,
                                       headers=register_apply_header,
                                       params=register_apply_param,
                                       data=register_apply_data)
print(register_apply_response.content.decode('utf-8'))
