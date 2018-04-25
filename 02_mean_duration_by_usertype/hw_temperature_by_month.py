import numpy as np
import matplotlib.pyplot as plt
import os

file = './hw_data.csv'
month_list = [1,2,3]
ndarr = np.loadtxt(file, delimiter=',', dtype='str', skiprows=1)
cln_data_arr = np.core.defchararray.replace(ndarr,' C','')

def bool_arr(cln_data_arr,month):
    bool_arr = ndarr[:,0]==month
    filtered_arr = cln_data_arr[bool_arr]
    return filtered_arr

# ndarr is read as str dtype, so month mun should be str
filtered_arr_m1 = bool_arr(cln_data_arr,'1')
filtered_arr_m2 = bool_arr(cln_data_arr,'2')
filtered_arr_m3 = bool_arr(cln_data_arr,'3')
filtered_list = [filtered_arr_m1,filtered_arr_m2,filtered_arr_m3]
temp_value_list = []
for filtered_arr in filtered_list:
    mean = np.mean(filtered_arr[:,-1].astype('float'))
    max = np.max(filtered_arr[:,-1].astype('float'))
    min = np.min(filtered_arr[:,-1].astype('float'))
    temp_value_list.append([mean,max,min])

i = 1
for item in temp_value_list:
    print('month {}, avr:{:.2f}, max:{}, min:{}'.format(i,item[0],item[1],item[2]))
    i+=1