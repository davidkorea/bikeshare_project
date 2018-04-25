import os
import numpy as np
import matplotlib.pyplot as plt

file_path = '../data'
# print(os.listdir(file_path))
filename_list = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
              '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']

def collect_and_process_data():
    cln_data_col_list = []
    for filename in filename_list:
        data_file = os.path.join(file_path,filename)
        data_arr = np.loadtxt(data_file,delimiter=',',dtype='str',skiprows=1)
        cln_data_col = np.core.defchararray.replace(data_arr[:,-1],'"','')
                       # 默认为行向量
        cln_data_col = cln_data_col.reshape(-1,1)
        cln_data_col_list.append(cln_data_col)
    year_member_type = np.concatenate(cln_data_col_list)
    return year_member_type

def analyse_data(year_member_type):
    n_member = year_member_type[year_member_type=='Member'].shape[0]
    n_casual = year_member_type[year_member_type=='Casual'].shape[0]
    n_users = [n_member,n_casual]
    return n_users

def save_and_show_results(n_users):
    plt.figure()
    plt.pie(n_users, labels=['Member','Casual'], autopct='%.2f%%',shadow=True,
            explode=(0.05,0))
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('./pie.png')
    plt.show()


year_member_type = collect_and_process_data()
n_users = analyse_data(year_member_type)
save_and_show_results(n_users)