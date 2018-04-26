import os
import numpy as np
import matplotlib.pyplot as plt

path = '../data'
# print(os.listdir(path))
filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
             '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']
hist_range = (0, 180)
n_bins = 12

def collect_data():
    new_dur_type_arr_list = []
    for filename in filenames:
        data_file = os.path.join(path, filename)
        data_arr = np.loadtxt(data_file,delimiter=',',dtype='str',skiprows=1)

        cln_duration_col = np.core.defchararray.replace(data_arr[:, 0],'"','').reshape(-1,1)
        cln_type_col = np.core.defchararray.replace(data_arr[:, -1],'"','').reshape(-1,1)
        #(815370, 1) | (815370, ).reshape(-1,1)=(815370, 1)
        # with no reshape, counld not concatenate(axis=1) as 'new_dur_type_arr'

        cln_dur_type_arr_list = [cln_duration_col,cln_type_col]

        new_dur_type_arr = np.concatenate(cln_dur_type_arr_list,axis=1)
        new_dur_type_arr_list.append(new_dur_type_arr)
    full_year_2col_data = np.concatenate(new_dur_type_arr_list) #(3758207, 2)

    m_duration_arr = full_year_2col_data[full_year_2col_data[:,-1]=='Member']
    c_duration_arr = full_year_2col_data[full_year_2col_data[:,-1]=='Casual']

    m_min_duration_arr = m_duration_arr[:,0].astype('float')/1000/60 #(2776393,)
    c_min_duration_arr= c_duration_arr[:,0].astype('float')/1000/60 #(981814,)

    return m_min_duration_arr,c_min_duration_arr

def analyse_data(m_min_duration_arr,c_min_duration_arr):
    m_dur_hist,m_bins_edges = np.histogram(m_min_duration_arr,range=hist_range,bins=n_bins)
    c_dur_hist,c_bins_edges = np.histogram(c_min_duration_arr,range=hist_range,bins=n_bins)
    # np.histogram() returns 2 vars...
    for i,j in zip(m_dur_hist,m_bins_edges):
        print('Member -> dur: {} - edge: {}'.format(i,j))
    for m,n in zip(c_dur_hist,c_bins_edges):
        print('Casual -> dur: {} - edge: {}'.format(m,n))

def save_and_show_results(m_min_duration_arr,c_min_duration_arr):
    fig = plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(1,2,1) #(row,culumn,position)
    ax2 = fig.add_subplot(1,2,2,sharey=ax1)

    ax1.hist(m_min_duration_arr,range=hist_range,bins=n_bins)
    ax1.set_xticks(range(0,181,15)) # from 0 to 180,step=15
    ax1.set_title('Member')
    ax1.set_ylabel('Count')

    ax2.hist(c_min_duration_arr,range=hist_range,bins=n_bins)
    ax2.set_xticks(range(0,181,15))
    ax2.set_title('Casual')
    ax2.set_ylabel('Count')

    plt.tight_layout()
    plt.savefig('./hist.png')
    plt.show()


m_min_duration_arr,c_min_duration_arr= collect_data()
analyse_data(m_min_duration_arr,c_min_duration_arr)
save_and_show_results(m_min_duration_arr,c_min_duration_arr)