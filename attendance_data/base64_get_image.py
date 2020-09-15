# -*- coding: utf-8 -*-

"""
Author:dongqiyun
Email:1808503589@qq.com

date:2020/9/11 15:26
"""

import os
import base64


def base64ToImage(txt_name):
    file_path = os.path.join(r'C:\Users\18085\Desktop', txt_name)
    with open(file_path, "r") as f:
        imgdata = base64.b64decode(f.read())
        file = open(os.path.join(r'C:\Users\18085\Desktop', txt_name+'.jpg'), 'wb')
        file.write(imgdata)
        file.close()


if __name__ == '__main__':
    base64ToImage('face')