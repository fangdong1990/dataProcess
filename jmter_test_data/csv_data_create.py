# -*- coding: utf-8 -*-

"""
Author:dongqiyun
Email:1808503589@qq.com

date:2020/9/15 17:01
"""

import csv
import random
import json
import os

"""
================================生成uid数据表======================================
"""


def csv_create_userdata_fromto(startc,count,filename):
    """
    生成指定数量的用户数据两列："usernamefrom", "usernameto"
    :param startc: 开始的数值
    :param conut: 一共写入多少用户数据
    :return:
    """
    ud = ""
    fileHeader = ["usernamefrom", "usernameto"]  # 定义文件头
    file_path = os.path.join(r"C:\Users\18085\Desktop\csv\base", filename)  # 打开指定文件
    csv_file = open(file_path, 'w')  # 打开文件
    writer = csv.writer(csv_file, lineterminator='\n')   # lineterminator='\n'可以消除空格
    writer.writerow(fileHeader)  # 写入头
    for i in range(startc, startc+count):
        if len(str(i)) == 1:
            ud = "000"+str(i)
        elif len(str(i)) == 2:
            ud = "00" + str(i)
        elif len(str(i)) == 3:
            ud = "0" + str(i)
        elif len(str(i)) == 4:
            ud = str(i)
        d = ["dqy" + ud, "dqy"+str(i+1000)]
        writer.writerow(d)
    csv_file.close()


def csv_create_userdata_only(startc,count,filename):
    """
    生成指定数量的用户数据一列：username
    :param startc: 开始的数值
    :param conut: 一共写入多少用户数据
    :return:
    """
    ud = ""
    fileHeader = ["uid_long_login"]  # 定义文件头
    file_path = os.path.join(r"C:\Users\18085\Desktop\csvdata\long_login", filename)   # 打开指定文件
    csv_file = open(file_path, 'w')  # 打开文件
    writer = csv.writer(csv_file, lineterminator='\n')   # lineterminator='\n'可以消除空格
    writer.writerow(fileHeader)  # 写入头
    for i in range(startc, startc+count):
        if len(str(i)) == 1:
            ud = "000"+str(i)
        elif len(str(i)) == 2:
            ud = "00" + str(i)
        elif len(str(i)) == 3:
            ud = "0" + str(i)
        elif len(str(i)) == 4:
            ud = str(i)
        d = ["dqy" + ud]
        writer.writerow(d)
    csv_file.close()


"""
======================================group数据处理：生成随机uidlsit=========================================
"""


def group_random_uidsList(filename,ownerId,minc,maxc):
    """
    根据指定文件filename生成不固定人员的随机数量人员群
    :return:slice：返回生成的群员列表
    """
    file_path = os.path.join(r"C:\Users\18085\Desktop\csvdata\not_login", filename)   # 打开指定文件
    csvFile = open(file_path, "r")
    reader = csv.reader(csvFile)
    aa = [json.dumps({"uid": item[0]}) for item in reader][1:]
    csvFile.close()
    slice = random.sample(aa, random.randint(minc, maxc))   # 随机生成群
    if json.dumps({"uid": ownerId}) not in slice:
        slice.append(json.dumps({"uid": ownerId}))
    return slice


"""
=========================================生成表===================================================
"""


def csv_create_group_random_uidslist_long_login(filename,startc,conut,filename_base,minc,maxc):
    """
    根据filename_based的值随机生成uidlist，filename为定义的新表，生成带群主的uidlist
    :param filename:定义新表
    :param startc:起始值
    :param conut:生成uid数量
    :param filename_base:根据filename_based的值随机生成uidlist
    :param minc:生成的uidlist长度下限
    :param maxc:生成的uidlist长度上限
    :return:
    """
    ud = ""
    fileHeader = ["uid_long_Login","uidsList_long"]                                                            # 定义文件头
    file_path = os.path.join(r"C:\Users\18085\Desktop\csvdata\new", filename)   # 打开指定文件
    csv_file = open(file_path, 'w')  # 打开文件
    writer = csv.writer(csv_file, lineterminator='\n')   # lineterminator='\n'可以消除空格
    writer.writerow(fileHeader)  # 写入头
    for i in range(startc, startc+conut):
        if len(str(i)) == 1:
            ud = "000"+str(i)
        elif len(str(i)) == 2:
            ud = "00" + str(i)
        elif len(str(i)) == 3:
            ud = "0" + str(i)
        elif len(str(i)) == 4:
            ud = str(i)
        d = ["dqy" + ud, group_random_uidsList(filename_base, "dqy" + ud, minc, maxc)]          # "dqy" + ud为群主
        writer.writerow(d)
    csv_file.close()


def csv_create_group_random_uidslist_not_login(filename,startc,conut,filename_base,minc,maxc):
    """
    根据filename_based的值随机生成uidlist，filename为定义的新表，生成带群主的uidlist
    :param filename:定义新表
    :param startc:起始值
    :param conut:生成uid数量
    :param filename_base:根据filename_based的值随机生成uidlist
    :param minc:生成的uidlist长度下限
    :param maxc:生成的uidlist长度上限
    :return:
    """
    ud = ""
    fileHeader = ["uid_not_Login","adduid","uidsList_not"]                                                            # 定义文件头
    file_path = os.path.join(r"C:\Users\18085\Desktop\csvdata\new", filename)   # 打开指定文件
    csv_file = open(file_path, 'w')  # 打开文件
    writer = csv.writer(csv_file, lineterminator='\n')   # lineterminator='\n'可以消除空格
    writer.writerow(fileHeader)  # 写入头
    for i in range(startc, startc+conut):
        if len(str(i)) == 1:
            ud = "000"+str(i)
        elif len(str(i)) == 2:
            ud = "00" + str(i)
        elif len(str(i)) == 3:
            ud = "0" + str(i)
        elif len(str(i)) == 4:
            ud = str(i)
        d = ["dqy" + ud,"dqy"+str(i+1000), group_random_uidsList(filename_base, "dqy" + ud, minc, maxc)]          # "dqy" + ud为群主
        writer.writerow(d)
    csv_file.close()

"""
==============================================批量生成数据表===========================================
"""


def create_500_only(numb):
    """
    生成numb个用户数据表10个,起始间隔500
    :param numb:
    :return:
    """
    for i in range(10):
        j = i*500+201
        csv_create_userdata_only(j, numb, "long_login_"+str(j)+"-"+str(j+numb-1)+".csv")


def create_500_fromto():
    """
    生成500用户数据表10个
    :return:
    """
    for i in range(10):
        j = i*500+101
        csv_create_userdata_fromto(j, 500, "username_fromto"+str(500)+"-"+str(j)+".csv")


def crate_lots_cvs_uidlist_long():
    """
    批量带随机uidlist的数据表:新创建表用户执行登录-发消息
    :return:
    """
    for i in range(10):
        j = i*500+1
        csv_create_group_random_uidslist_long_login("long_login_"+str(j+200)+"-"+str(j+500-1)+".csv", j+200, 300, "not_login_"+str(j)+"-"+str(j+100-1)+".csv", 5, 100)


def crate_lots_cvs_uidlist_not_login():
    """
    批量带随机uidlist的数据表:新创建表用户不登录
    :return:
    """
    for i in range(10):
        j = i*500+1
        csv_create_group_random_uidslist_not_login("not_login_"+str(j)+"-"+str(j+100-1)+".csv", j, 100, "not_login_"+str(j)+"-"+str(j+100-1)+".csv", 5, 100)


if __name__ == "__main__":
    crate_lots_cvs_uidlist_not_login()







