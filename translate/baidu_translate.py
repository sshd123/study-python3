# -*- coding: utf-8 -*-
# http://api.fanyi.baidu.com/api/trans/product/apidoc

import hashlib
import json
import random

import requests

server_url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
app_id = '*****'
app_secret = '*****'


def get_random():
    return random.randint(0, 65536)


def sign(q, salt):
    sign_str = app_id + q + str(salt) + app_secret
    m2 = hashlib.md5()
    m2.update(sign_str.encode('utf-8'))
    return m2.hexdigest()


class Api(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def translate(data, from_language, to_language):
        salt = get_random()
        payload = {"q": data, "from": from_language, "to": to_language, "appid": app_id, "salt": salt,
                   "sign": sign(data, salt)}
        r = requests.get(server_url, params=payload)
        response = json.loads(r.content, encoding='utf-8')
        trans_result = response['trans_result'][0]
        return trans_result['src'], trans_result['dst'],


if __name__ == '__main__':
    src, dst = Api.translate("査詢", "cht", "zh")
    print('{}=>{}'.format(src, dst))
