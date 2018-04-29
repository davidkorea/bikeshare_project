import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

def chinese():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


data_file = './hw_data_temp.csv'
# print(os.path.exists(data_file))
month_list = ['1','2','3']

def data_collect():
    above_list = []
    below_list = []

    data_arr= np.loadtxt(data_file,delimiter=',',dtype='str',skiprows=1)
    cln_data_arr = np.core.defchararray.replace(data_arr,' C','')

    for month in month_list:
        month_data_arr = cln_data_arr[cln_data_arr[:,0]==month]
        month_above_num = month_data_arr[month_data_arr[:,1]>='0'].shape[0]
        month_below_num = month_data_arr[month_data_arr[:,1]<'0'].shape[0]
        above_list.append(month_above_num)
        below_list.append(month_below_num)
    return above_list,below_list

def plot(above_list,below_list):
    bar_locs = np.arange(3)
    bar_width = 0.35
    xticks_label = ['{}月份'.format(i+1) for i in range(3)]

    plt.figure()
    plt.bar(bar_locs,above_list,width=bar_width,color='r',alpha=0.7,label='零上')
    plt.bar(bar_locs+bar_width,below_list,width=bar_width,color='b',alpha=0.7,label='零下')

    plt.xticks(bar_locs+bar_width/2,xticks_label,fontproperties=chinese())
    plt.ylabel('天数',fontproperties=chinese())
    plt.title('每月气温零上零下对比图',fontproperties=chinese())
    plt.legend(loc='best',prop=chinese())

    plt.tight_layout()
    plt.savefig('./hw_temp_bar_1.png')
    plt.show()


above_list,below_list = data_collect()
plot(above_list,below_list)
