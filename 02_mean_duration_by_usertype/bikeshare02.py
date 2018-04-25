import os
import numpy as np
import matplotlib.pyplot as plt

data_path = '../data'
data_filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
              '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']
# print(os.listdir(data_path))

def collect_and_process_data():
    cln_data_arr_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path,data_filename)
        data_arr = np.loadtxt(data_file,delimiter=',',dtype='str',skiprows=1)

        cln_data_arr = np.core.defchararray.replace(data_arr,'"','')
        cln_data_arr_list.append(cln_data_arr)
    return cln_data_arr_list

def get_mean_duration_by_type(cln_data_arr_list,type):
    mean_duration_list = []
    for data_arr in cln_data_arr_list:
        bool_arr = data_arr[:,-1]==type
        filtered_arr = data_arr[bool_arr]

        mean_duration = np.mean(filtered_arr[:,0].astype('float')/1000/60)
        mean_duration_list.append(mean_duration)
    return mean_duration_list

def save_and_show_results(member_mean_duration_list,casual_mean_duration_list):

    for idx in range(len(member_mean_duration_list)):
        member_mean_duration = member_mean_duration_list[idx]
        casual_mean_duration = casual_mean_duration_list[idx]
        print('Quarter {}: member avr is {:.2f}min, casual avr is {:.2f}min'.format(
            idx+1, member_mean_duration, casual_mean_duration
        ))

    mean_duration_arr = np.array([member_mean_duration_list, casual_mean_duration_list]).transpose()
    np.savetxt('./mean_duration.csv', mean_duration_arr, delimiter=',',
               header='Member mean duration, Casual mean duration', fmt='%.4f', comments='')

    plt.figure()
    plt.plot(member_mean_duration_list, color='g', linestyle='-', marker='o', label='Member')
    plt.plot(casual_mean_duration_list,color='r', linestyle='--', marker='*', label='Casual')
    plt.title('Member vs Casual')
    plt.xlabel('Quarter')
    plt.ylabel('Mean duration(min)')
    plt.xticks(range(0,4),['1st','2nd','3rd','4th'],rotation=45)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('./plot.png')
    plt.show()

cln_data_arr_list = collect_and_process_data()
member_mean_duration_list = get_mean_duration_by_type(cln_data_arr_list,'Member')
casual_mean_duration_list = get_mean_duration_by_type(cln_data_arr_list,'Casual')
save_and_show_results(member_mean_duration_list,casual_mean_duration_list)