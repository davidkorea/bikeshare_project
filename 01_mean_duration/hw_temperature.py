import numpy as np

data_path = '/Users/osx/Desktop/bikeshare/hw_data.csv'
def process_data():
    data_file = np.loadtxt(data_path, delimiter=',', dtype='str', skiprows=1)
    tem_str_col = data_file[:,1]
    tem_str_c = np.core.defchararray.replace(tem_str_col,' C','')
    # print(tem_str_c)
    tem_str_f = tem_str_c.astype('float') * 1.8 + 32
    for i,j in zip(tem_str_c,tem_str_f):
      print('{}C -> {:.1f}F'.format(i,j))

process_data()