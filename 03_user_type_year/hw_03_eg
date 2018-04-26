# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 1. 读取csv数据文件
data_arr1 = np.loadtxt('./201801_temp.csv', delimiter=',', skiprows=1)
data_arr2 = np.loadtxt('./201802_temp.csv', delimiter=',', skiprows=1)
data_arr3 = np.loadtxt('./201803_temp.csv', delimiter=',', skiprows=1)

# 2. 数组合并
combined_data_arr = np.concatenate([data_arr1, data_arr2, data_arr3])

# 3. 使用布尔型数组数据过滤
# 获取零上气温的天数
# shape返回行数和列数，第0个元素是行数，即记录个数
n_positive_days = combined_data_arr[combined_data_arr >= 0].shape[0]

# 获取零下气温的天数
n_negative_days = combined_data_arr[combined_data_arr < 0].shape[0]

n_days = [n_positive_days, n_negative_days]

# 4. 进行饼状图可视化占比
plt.figure()
plt.pie(n_days, labels=['>=0', '<0'], autopct='%.2f%%')
plt.axis('equal')
plt.tight_layout()
plt.show()
