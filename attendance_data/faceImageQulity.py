# -*- coding: utf-8 -*-

"""
Author:dongqiyun
Email:1808503589@qq.com

date:2020/8/26 16:17
"""

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import os

"""
=====================================获取数据=========================================
"""


def face_image_qulity():
    """输出数据list格式"""
    image_list = []
    file_path = os.path.join(r"C:\Users\18085\Desktop", "face_ImageQuality.txt")
    with open(file_path, 'r', encoding='utf-16') as f:
        for line in f:
            if "Param" in line:
                image_data = float(line.split('current:')[-1].split('==Param')[0])*100
                image_list.append(image_data)

    print(len(image_list))
    return image_list


"""
=============================使用获取到的数据画图========================================
"""
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False
style.use('ggplot')


def face_image_plot_hist():
    """
    直方图hist，用于统计某个区间的显示
    """
    # 随机定义了年龄
    # bins用于设置区间,即10岁一个区间
    y_list = face_image_qulity()
    bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    plt.hist(y_list, bins, rwidth=0.8, label="采样数值："+str(len(y_list)))   # 画直方图
    plt.title('人脸质量检测结果')
    plt.xlabel("人脸检测数值")
    plt.ylabel("人脸检测结果对应样本数")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # a = face_image_qulity()
    # print(a)
    face_image_plot_hist()