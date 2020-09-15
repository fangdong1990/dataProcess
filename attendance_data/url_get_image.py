# -*- coding: utf-8 -*-

"""
Author:dongqiyun
Email:1808503589@qq.com

date:2020/9/15 11:26
"""


import csv
import urllib.request
import os


def read_csv():
    csv_file = r'C:\Users\18085\Desktop\whitelistdb.csv'
    with open(csv_file, 'r') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            # print(line)
            try:
                url_get_imgage(line[0], line[1])
            except:
                print(line)


def url_get_imgage(img_src, image_name):
    # 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
    urllib.request.urlretrieve(img_src, os.path.join(r'C:\Users\18085\Desktop\face_image', str(image_name)+'.jpg'))


if __name__ == "__main__":
    read_csv()
