# -*- coding: utf-8 -*-

"""
Author:dongqiyun
Email:1808503589@qq.com

date:2020/9/17 11:28
"""

import csv
import os.path
import requests
import json
import time


def request_face_api(name,faceurl,userid):
    headers_ = {"Content-Type": "application/json", }
    url_ = 'http://192.168.11.233:30290/v1/tdEmployee/getPushEmployeeListByDeviceId'
    data_ = {
        "deviceCode": "0E446ABAA506",
        "data": [
            {
                "userId": userid,
                "name": name,
                "photo": faceurl,
                "type": "1"
            }
        ]
    }
    r = requests.post(url=url_, data=json.dumps(data_), headers=headers_)
    # result = json.dumps(r.json(), sort_keys=True, indent=4, ensure_ascii=False)
    if r.json()["code"] == 200:
        pass
    else:
        print(r.json())
        # requests.post(url=url_, data=json.dumps(data_), headers=headers_)


csv_path = os.path.join(r'C:\Users\18085\Desktop', 'whitelistdb.csv')
with open(csv_path, 'r', encoding='utf-8') as f:
    csv_read = csv.reader(f)
    for csv_line in csv_read:
        request_face_api(csv_line[2], csv_line[0], csv_line[1])
        time.sleep(0.2)
        # print(csv_line)


