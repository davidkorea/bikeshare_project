import numpy as np

month_list = ['1','2','3']
data_arr = np.loadtxt('./hw_data.csv',delimiter=',',dtype='str', skiprows=1)
cln_data_arr = np.core.defchararray.replace(data_arr,' C','')
for month in month_list:
    bool_arr = cln_data_arr[:,0] == month
    filtered_arr = cln_data_arr[bool_arr]
    mean = np.mean(filtered_arr[:,-1].astype('float'))
    max = np.max(filtered_arr[:,-1].astype('float'))
    min = np.min(filtered_arr[:,-1].astype('float'))
    print('month{}: mean = {:.2f}, max = {:.2f}, min = {:.2f}'.format(month,mean,max,min))