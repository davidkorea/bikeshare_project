import os
import numpy as np
import matplotlib.pyplot as plt
# from pylab import *
# mpl.rcParams['font.sans-serif'] = ['SimHei']

data_path= './hw_data_temp'
# print(os.listdir(data_path))
file_names = ['201801_temp.csv', '201802_temp.csv', '201803_temp.csv']

def collect_data():
    temp_col_list = []
    for file in file_names:
        data_file = os.path.join(data_path,file)
        temp_col = np.loadtxt(data_file, delimiter=',',skiprows=1)
        temp_col_list.append(temp_col)
    all_list = np.concatenate(temp_col_list)
    return all_list

def analyse_data(all_list):
    upper = all_list[all_list < 0].shape[0]
    lower = all_list[all_list >= 0].shape[0]
    temp_n = [upper, lower]
    return temp_n

def save_and_show_results(temp_n):
    plt.figure()
    plt.pie(temp_n, labels=['> 0', '< 0'], autopct='%.2f%%',
            shadow=True,explode=(0.05,0))
    plt.axis('equal')
    plt.title('Temp ratio in 1~3month')
    plt.tight_layout()
    plt.savefig('./hw_pie.png')
    plt.show()


all_list = collect_data()
temp_n = analyse_data(all_list)
save_and_show_results(temp_n)