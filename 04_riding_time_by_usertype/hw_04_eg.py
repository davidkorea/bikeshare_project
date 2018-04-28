# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 读取csv数据文件
data_arr = np.loadtxt('./hw_data_temp.csv', delimiter=',', skiprows=1)

# 1. 统计直方图所需信息
# 气温数据
temp_arr = data_arr[:, 1]

# 统计的数据范围范围
hist_range = (-10, 10)

# 分桶个数
n_bins = 5

# 2. 直方图统计
stats, bin_edges = np.histogram(temp_arr, range=hist_range, bins=n_bins)
print('气温直方图统计信息：{}, 直方图分组边界:{}'.format(stats, bin_edges))

# 3. 可视化直方图
plt.figure()
plt.hist(temp_arr, range=hist_range, bins=n_bins)
# 设置x轴坐标点显示为分组边界
plt.xticks(bin_edges)
plt.show()
