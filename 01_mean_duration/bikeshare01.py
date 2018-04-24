import numpy as np
import matplotlib.pyplot as plt
import os

data_path = '/Users/osx/Desktop/bikeshare/data'
data_filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
              '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']

def collect_data():
    data_arr_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path,data_filename)
        data_arr = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)
        data_arr_list.append(data_arr)
        # print(len(data_arr_list))
    return data_arr_list

def process_data(data_arr_list):
    duration_in_min_list = []
    for data_arr in data_arr_list:
        duration_str_col = data_arr[:,0]
        duration_in_ms = np.core.defchararray.replace(duration_str_col, '"', '')
        duration_in_min = duration_in_ms.astype('float') / 1000 / 60
        duration_in_min_list.append(duration_in_min)
    return duration_in_min_list

def analyze_data(duration_in_min_list):
    duration_mean_list = []
    for i, duration_arr in enumerate(duration_in_min_list):
        duration_mean = np.mean(duration_arr)
        duration_mean_list.append(duration_mean)
        print('the quarter{} avr time is {:.2f}'.format(i+1,duration_mean))
    return duration_mean_list

def show_results(duration_mean_list):
    plt.figure()
    plt.bar(range(len(duration_mean_list)),duration_mean_list)
    plt.show()




data_arr_list = collect_data()
duration_in_min_list = process_data(data_arr_list)
duration_mean_list = analyze_data(duration_in_min_list)
show_results(duration_mean_list)
