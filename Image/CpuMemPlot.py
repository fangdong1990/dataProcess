# -*- coding: utf-8 -*-

"""
Author:dongqiyun
Email:1808503589@qq.com

date:2020/8/26 11:24
"""


from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import os

"""
=====================================获取cpu、内存数据=========================================
"""


def cpu_list(file_name, package_name):
    """输出cpu数据list格式"""
    cpu_list = []
    file_path = os.path.join(r"C:\Users\18085\Desktop", file_name)
    for line in open(file_path):
        if package_name in line:
            cuplist = line.split(" ")  # 使用空格切割返回的字符串
            while '' in cuplist:
                cuplist.remove('')  # 将list中的空元素删除
            cpu_ = int(cuplist[4].strip('%'))  # 去掉%
            cpu_list.append(cpu_)
    return cpu_list


def mem_list(file_name, package_name):
    """输出内存数据list格式"""
    mem_list = []
    file_path = os.path.join(r"C:\Users\18085\Desktop", file_name)
    for line in open(file_path):
        if package_name in line:
            cuplist = line.split(" ")  # 使用空格切割返回的字符串
            while '' in cuplist:
                cuplist.remove('')  # 将list中的空元素删除
            rss_ = cuplist[8].strip('K')
            mem = int(int(rss_) / 1024)
            mem_list.append(mem)
    return mem_list


"""
=============================使用获取到的数据画图========================================
"""
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False
style.use('ggplot')


def cpu_mem_plot():
    fig = plt.figure()

    # 添加cpu图像
    ax_cpu = fig.add_subplot(211)
    cpu_y = cpu_list("cpu_mem_3", "com.frame.tdweilai.attendance")          # 定义纵坐标
    cpu_x = np.arange(0, len(cpu_y), 1)                                     # 定义横坐标
    ax_cpu.plot(cpu_x, cpu_y, label='CPU占比(%)')
    ax_cpu.legend(loc=1)                                                    # 显示label
    ax_cpu.set_title("24小时：考勤应用程序占用系统CPU情况统计")             # 运行24小时是8640个样本数据

    # 添加mem图像
    ax_mem = fig.add_subplot(212)
    mem_y = mem_list("cpu_mem_3", "com.frame.tdweilai.attendance")          # 定义纵坐标
    mem_x = np.arange(0, len(mem_y), 1)                                     # 定义横坐标
    ax_mem.plot(mem_x, mem_y, label='内存占用(M)', color="b")
    ax_mem.legend(loc=1)                                                    # 显示label
    ax_mem.set_title("24小时：考勤应用程序占用系统内存情况统计")

    # 显示图像
    plt.show()


if __name__ == "__main__":
    cpu_mem_plot()
