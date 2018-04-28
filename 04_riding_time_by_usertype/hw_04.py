import os
import numpy as np
import matplotlib.pyplot as plt
file_path = './hw_data_temp'
# print(os.listdir('./hw_data_temp'))
file_names = ['201801_temp.csv', '201802_temp.csv',
              '201803_temp.csv']

def collect_data():
    data_arr_list = []
    for file_name in file_names:
        file_full_path = os.path.join(file_path,file_name)
        data_arr = np.loadtxt(file_full_path,delimiter=',',skiprows=1)
        data_arr_list.append(data_arr)

    return data_arr_list

def analyse_data(data_arr_list):
    i=1
    for month in data_arr_list:
        temp,edge = np.histogram(month,range=(-10,10),bins=4)
        print("month: {} - temp: {}, edge : {}".format(i,temp,edge))
        i+=1

def plot(data_arr_list):
    fig = plt.figure(figsize=(9,3))
    ax1 = fig.add_subplot(1,3,1)
    ax2 = fig.add_subplot(1,3,2,sharey=ax1)
    ax3 = fig.add_subplot(1,3,3,sharey=ax1)

    ax1.hist(data_arr_list[0], range=(-10, 10), bins=4)
    ax1.set_xticks(range(-10,10,5))
    ax2.hist(data_arr_list[1], range=(-10, 10), bins=4)
    ax2.set_xticks(range(-10,10,5))
    ax3.hist(data_arr_list[2], range=(-10, 10), bins=4)
    ax3.set_xticks(range(-10,10,5))
    
    fig.tight_layout()
    fig.show()







data_arr_list = collect_data()
analyse_data(data_arr_list)
plot(data_arr_list)