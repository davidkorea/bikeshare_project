# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 读取csv数据文件
data_arr = np.loadtxt('./hw_data_temp.csv', delimiter=',', skiprows=1)

month_list = [1, 2, 3]

# 初始化零上、零下气温的天数
n_positive_days_list = []
n_negative_days_list = []

for month in month_list:
    # 1. 根据月份过滤获取每月气温数据
    month_arr = data_arr[:, 0] == month
    month_temp_arr = data_arr[month_arr][:, 1]

    # 2. 对比0获得零上、零下气温天数
    n_positive_days = month_temp_arr[month_temp_arr >= 0].shape[0]
    n_negative_days = month_temp_arr[month_temp_arr < 0].shape[0]

    # 添加到列表中
    n_positive_days_list.append(n_positive_days)
    n_negative_days_list.append(n_negative_days)

# 3. 分组柱状图绘制
# 每组柱子的位置，3个月的数据
bar_locs = np.arange(3)
# 坐标轴标签
xtick_labels = np.arange(1, 4)
# 柱子宽度
bar_width = 0.35

plt.figure()
# 第一组柱状图
plt.bar(bar_locs, n_positive_days_list, width=bar_width, color='g', alpha=0.7, label='>=0')
# 第二组柱状图，注意添加了“偏移量”，即bar_width
plt.bar(bar_locs + bar_width, n_negative_days_list, width=bar_width, color='r', alpha=0.7, label='<0')
plt.xticks(bar_locs + bar_width / 2, xtick_labels)
plt.legend(loc='best')
plt.show()
