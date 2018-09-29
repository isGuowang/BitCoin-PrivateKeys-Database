# coding:utf-8
import requests
import json
import time


def dictget(b, obj, default=None):
    for k, v in b.items():
        if k == obj:
            return  v

        else:
            if type(v) is dict:
                re = dictget(v, obj)
                if re is not default:
                    return re


def btcApi(address):
    data = address
    response = requests.get("https://chain.api.btc.com/v3/address/" + data)
    a = response.text
    b = json.loads(a)
    c = dictget(b, 'balance')
    time.sleep(0.53)
    return c


