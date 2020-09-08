# -*- coding: utf-8 -*-

"""
Author:dongqiyun
Email:1808503589@qq.com

date:2020/8/28 16:20
"""

import pandas as pd
import matplotlib.pyplot as plt
aa = 'r./data/data1.xls'
df = pd.DataFrame(pd.read_excel(aa))
# 分组统计排序
# 通过reset_index()函数将groupby()的分组结果重新设置索引
df1 = df.groupby(["图书编号"])[买家实际支付金额].sum().reset_index()
df1 = df1.set_index('图书编号')	# 设置索引
df1 = df1[u'买家实际支付金额'].copy()
df2 = df1.sort_values(ascending = False)
# 图表字体为华文细黑，字号10
plt.rc('font', family = 'SimHei', size = 10)
plt.figure('贡献度分析')
df2.plot(kind = 'bar')
plt.ylabel(u'销售收入（元）')
p = 1.0*df2.cumsum() / df2.sum()
print(p)
p.plot(color = 'r', secondary_y = True, style = '-o', linewidth = 0.5)
plt.annotate(format(p[9],'.4%'), xy = (9,p[9]), xytext = (9*0.9, p[9]*0.9),
	    # 添加标记，并且指定箭头样式
	    arrowprops = dict(arrowstyle = "->",connectionstyle = "arc3,rad = .1"))
plt.ylabel(u'收入（比例）')
plt.show()