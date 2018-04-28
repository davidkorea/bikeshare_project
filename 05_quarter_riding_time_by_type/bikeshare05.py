import os
import numpy as np
import matplotlib.pyplot as plt

file_path = '../data'
print(os.listdir(file_path))
file_names = ['2017-q1_trip_history_data.csv',
              '2017-q2_trip_history_data.csv',
              '2017-q3_trip_history_data.csv',
              '2017-q4_trip_history_data.csv']

def collect_data():
    mean_member_list = []
    mean_casual_list = []
    for file_name in file_names:
        data_file = os.path.join(file_path,file_name)
        data_arr = np.loadtxt(data_file,delimiter=',',dtype='str',skiprows=1)
        cln_dur_col = np.core.defchararray.replace(data_arr[:,0],'"','').reshape(-1,1)
        cln_type_col = np.core.defchararray.replace(data_arr[:,-1],'"','').reshape(-1,1)
        # dur_type_arr = np.array(cln_dur_col,cln_type_col)
        dur_type_arr = np.concatenate([cln_dur_col,cln_type_col],axis=1)

        #mask
        member_dur_arr = dur_type_arr[dur_type_arr[:,1]=='Member']
        casual_dur_arr = dur_type_arr[dur_type_arr[:,1]=='Casual']

        #mean
        mean_member = np.mean(member_dur_arr[:,0].astype('float')/1000/60)
        mean_member_list.append(mean_member)
        mean_casual = np.mean(casual_dur_arr[:,0].astype('float')/1000/60)
        mean_casual_list.append(mean_casual)

    return mean_member_list,mean_casual_list
    # mean_member_list = [11.51173404858448, 12.39381192932041,
    #                     12.590282204738374, 11.922725559957398]
    # mean_casual_list = [40.76690234804407, 40.93548325768106,
    #                     38.42203748802542, 36.12188032420145]

def plot(mean_member_list,mean_casual_list):
    bar_locs = np.arange(4)
    bar_width = 0.35

    plt.figure()
    plt.bar(bar_locs,mean_member_list, width=bar_width,color='b',alpha=0.7,label='会员')
    plt.bar(bar_locs+bar_width,mean_casual_list, width=bar_width,color='g',alpha=0.7,label='非会员')
    # plt.bar() 前两个参数顺序不能变

    plt.ylabel('平均骑行时间（分钟）')
    plt.title('会员/非会员骑行时间季度柱状图')
    plt.legend(loc='best')

    plt.tight_layout()
    plt.savefig('./group_bar.png')
    plt.show()


mean_member_list,mean_casual_list = collect_data()
plot(mean_member_list,mean_casual_list)