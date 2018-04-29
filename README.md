> repo정리하기 때문에 어제한 컨트리뷰션스 다 없어졌네ㅠㅠ

# bikeshare
Everage riding time for each quarter in 2017
 
# Issue 1 - .gitignore
 
If the size of a sigle file is bigger than 50M, could not be uploaded to github.

Before you add files to .git, make .gitignore first and then it could work and ignore the files you added to .gitignore

```
$ git clone 
$ cd bikeshare
$ touch .gitignore
$ vim .gitignore
$ data -> 'ESC'
$ :wq
```

# Issue 2 - git init Desktop

잘못으로 바탕화면을 git repo로 추가했음..ㅠ 아래 코드에 따라 해결할수있음.

```
$ cd desktop
$ rm -rf .git
```

# 01 mean duration

  * file path
  ```php 
  data_file = os.path.join(path,file_name)
  ```
  * read file 
  ```php
  read_file = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)  //n demention array N维数组
  ```
  * read columns 
  ```php
  needed_column = read_file[:, 1] //[row,column], [;, 1] all rows' No. 1 column(starts from No. 0).
  ``` 
  * clean data 
  ```php
  clean_col_data = np.core.defchararray.replace(needed_column, 'xxx', 'yyy') //change 'xxx' to 'yyy'.
  ```
  * change data type
  ```php
  change_data_type = clean_col_data.astype('float')
  ```
  * calculate
  ```php
  calculate = change_data_type * 100
  ```

# 02 mean duration by user tupe
 
## Subject

  - filter data by boolean array
  
    - get ndarray
      ```php
      data_arr = np.loadtxt('./path', delimiter=',', dtype='str', skiprows=1)
      ```
    - clean data
      ```php
      cln_data_arr = np.core.defchararray.replace(data_arr, ' C', '')
      ```
    - boolean/mask array
      ```php
      bool_arr = cln_data_arr[:, 0] == 'Jan' // 1-demention, only 1 column
      ```
    - filtered_arr
      ```php
      filtered_arr = cln_data_arr[bool_arr] // 2-demention, same demention as origin data
      ```
      
    > How to use different demention mask to sort data? how to know which column should apply a mask??
      
      
    ![](https://github.com/davidkorea/bikeshare_project/blob/master/images/datafliter.jpg?raw=true)
    
    ![](https://github.com/davidkorea/bikeshare_project/blob/master/images/guangbo.jpg?raw=true)

    
  - create a n-demention array ndarray
    
    Using list's list to create a n demention array.
    ```php
    create_ndarray = np.array( [list1, list2, ... ] )
    ```
  
  - matplotlib
  
### 1. filter data by boolean array

Debug logs 

```python
>>>data_arr
Out[1]: 
array([['221834', '2017-01-01 00:00:41', '2017-01-01 00:04:23', ...,
        'M St & New Jersey Ave SE', 'W00869', 'Member'],
       ['1676854', '2017-01-01 00:06:53', '2017-01-01 00:34:49', ...,
        '8th & D St NW', 'W00894', 'Casual'],
       ['1356956', '2017-01-01 00:07:10', '2017-01-01 00:29:47', ...,
        'New York Ave & 15th St NW', 'W21945', 'Casual'],
       ...,
       ['423494', '2017-03-31 23:58:34', '2017-04-01 00:05:38', ...,
        '11th & H St NE', 'W20773', 'Member'],
       ['1048876', '2017-03-31 23:59:33', '2017-04-01 00:17:02', ...,
        'Potomac & Pennsylvania Ave SE', 'W20784', 'Member'],
       ['223449', '2017-03-31 23:59:43', '2017-04-01 00:03:26', ...,
        '16th & Harvard St NW', 'W20825', 'Member']], dtype='<U64')
        
>>>data_arr.shape
Out[2]: (646586, 9)

>>>bool_arr
Out[3]: array([ True, False, False, ...,  True,  True,  True])

>>>bool_arr.shape
Out[4]: (646586,)

>>>filtered_arr.shape
Out[5]: (528509, 9)

>>>filtered_arr
Out[6]: 
array([['221834', '2017-01-01 00:00:41', '2017-01-01 00:04:23', ...,
        'M St & New Jersey Ave SE', 'W00869', 'Member'],
       ['473337', '2017-01-01 00:08:36', '2017-01-01 00:16:29', ...,
        '3rd & H St NE', 'W20340', 'Member'],
       ['200077', '2017-01-01 00:11:07', '2017-01-01 00:14:27', ...,
        'Calvert St & Woodley Pl NW', 'W20398', 'Member'],
       ...,
       ['423494', '2017-03-31 23:58:34', '2017-04-01 00:05:38', ...,
        '11th & H St NE', 'W20773', 'Member'],
       ['1048876', '2017-03-31 23:59:33', '2017-04-01 00:17:02', ...,
        'Potomac & Pennsylvania Ave SE', 'W20784', 'Member'],
       ['223449', '2017-03-31 23:59:43', '2017-04-01 00:03:26', ...,
        '16th & Harvard St NW', 'W20825', 'Member']], dtype='<U64')

```

* ```data_arr```: cleaned data with no "".
* ```data_arr.shape = (646586, 9)```: same demention as raw data.
* ```bool_arr```: through ```data_arr[:, -1] == type```, select only the last one column and return/change it to the boolean array. Also it it a one demention array,because we select only one(last) column.that why ```bool_arr.shape = (646586,)```
* when we process x[y], the mask array (bool_arr) will be expanded automatically as the same demention as the raw data(array x). another words, (646586, 9) + (646586, ) = (528509, 9)/filtered_arr 

### 2. save & show results

* create ndarray and save as csv

```php
mean_duraion_arr = np.array([member_mean_duration_list, casual_mean_duration_list])
np.savetxt('./mean_duration.csv', mean_duraion_arr, delimiter=',')
```
![](https://github.com/davidkorea/bikeshare_project/blob/master/images/csv.png)

* matplotlab 

```php
 plt.figure()
 plt.plot(member_mean_duration_list, color='g', linestyle='-', marker='o', label='Member')
 plt.plot(casual_mean_duration_list, color='r', linestyle='--', marker='*', label='Casual')
 plt.title('Member vs Casual')
 plt.xlabel('Quarter')
 plt.ylabel('Mean duration (min)')
 plt.legend(loc='best')
 plt.savefig('./duration_trend.png')
 plt.show()
```
![](https://github.com/davidkorea/bikeshare_project/blob/master/images/plot1.png)

**>>> optimize code**

* transfer csv to 4rows,2colums format
```php
mean_duraion_arr = np.array([member_mean_duration_list, casual_mean_duration_list]).transpose()
```
* add header for csv
```php
np.savetxt('./mean_duration.csv', mean_duraion_arr, delimiter=',',
           header='Member Mean Duraion, Casual Mean Duraion', fmt='%.4f',
           comments='')
```
if no ```comments=''```, the header will start with a "#" sign which means the first row is being commented by default.
![](https://github.com/davidkorea/bikeshare_project/blob/master/images/csv2.png)

* plot xticks
```php
plt.xticks(range(0, 4), ['1st', '2nd', '3rd', '4th'], rotation=45)

```
* tight layout
```php
plt.tight_layout()
```
otherwise, the layout couldn't show a full page, x-label has been cut.
![](https://github.com/davidkorea/bikeshare_project/blob/master/images/plot2.png)
 
# 03 Pie chart by user type percentage

### 1. n-array reshape / concatenate

* Reshape - array's demention could be changed by the condtion which is keeping the ammount of data. 

  > A[ i , j ] = B[ m , n ], i x j = m x n.
  
  ```php
  arr_a.shape() = (3,4)
  arr_a = arr_a.reshape(1,12) or arr_a.reshape(6,2)
  arr_a = arr_a.reshape(-1,1) //'-1'could be calcuated by python and equals 12
  ```
  
  if you just know one demention of the new array, you can use '-1' to represent it as the other demention.
  
  ![](https://github.com/davidkorea/bikeshare_project/blob/master/images/reshape.png)

* Concatenate - if some arrays have same culumn-dementons, they could be binded as a new array.

  ![](https://github.com/davidkorea/bikeshare_project/blob/master/images/concatenate1.png)
  
### 2. pie chart

```php
n_users = [n_member, n_casual]

plt.figure()
plt.pie(n_users, labels=['Member', 'Casual'], autopct='%.2f%%', shadow=True, explode=(0.05, 0))
plt.axis('equal') // let x = y to make a round circle pie chart.
plt.tight_layout() //make all the things into this figure.
plt.savefig('./xxx.png')
plt.show()

```

# 04 Histogram chart of riding time by user type

## Subject
* reshape / concatenate
* np.histogram
* plt.add_subplot

  ![](https://github.com/davidkorea/bikeshare_project/blob/master/images/histogram.png)

### 1. reshape / concatenate

```php
cln_duration_col = np.core.defchararray.replace(data_arr[:, 0],'"','').reshape(-1,1)
cln_type_col = np.core.defchararray.replace(data_arr[:, -1],'"','').reshape(-1,1)
#(815370, 1) | (815370, ).reshape(-1,1)=(815370, 1)
# with no reshape, could not concatenate(axis=1) as 'new_dur_type_arr' -> below **Error**
cln_dur_type_arr_list = [cln_duration_col,cln_type_col]
new_dur_type_arr = np.concatenate(cln_dur_type_arr_list,axis=1)
```
> **Error**
> all_data_arr = np.concatenate(data_arr_list,axis=1)
> numpy.core._internal.AxisError: axis 1 is out of bounds for array of dimension 1

* get one column data as a column vector
  
  cln_dur_col -> cln_dur_col.reshape(-1,1)   |   (815370, ).reshape(-1,1)=(815370, 1)
  
* make a new array by needed column data

  np.concatenate(cln_dur_col, cln_type_col, axis=1), (815370, 2) 
  
### 2. no.histogram

```php
hist_range = (0, 180)
n_bins = 12
m_dur_hist,m_bins_edges = np.histogram(m_min_duration_arr,range=hist_range,bins=n_bins)
# np.histogram() returns 2 vars...
```
### 3. np.hist / add_subplot

```php
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1) #(row,culumn,position)
ax2 = fig.add_subplot(1,2,2,sharey=ax1)

ax1.hist(m_min_duration_arr,range=hist_range,bins=n_bins)
ax1.set_xticks(range(0,181,15)) # from 0 to 180,step=15
ax1.set_title('Member')
ax1.set_ylabel('Count')
```
# 05 Grouped bar chart & quarter riding time by type

### Chinese font

```php
from matplotlib.font_manager import FontProperties
def get_chinese_font():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
```

### Grouped bar chart

```php
  bar_locs = np.arange(4)
  bar_width = 0.35
+ xticks_labels = ['第{}季度'.format(i+1) for i in range(4)]

  plt.figure()
  plt.bar(bar_locs,mean_member_list, width=bar_width,color='b',alpha=0.7,label='会员')
  plt.bar(bar_locs+bar_width,mean_casual_list, width=bar_width,color='g',alpha=0.7,label='非会员')
  # plt.bar() 前两个参数顺序不能变

+ plt.xticks(bar_locs + bar_width/2,xticks_labels,rotation=45,fontproperties=get_chinese_font())
  plt.ylabel('平均骑行时间（分钟）', fontproperties=get_chinese_font())
  plt.title('会员/非会员骑行时间季度柱状图',fontproperties=get_chinese_font())
  plt.legend(loc='best',prop=get_chinese_font())

  plt.tight_layout()
  plt.savefig('./group_bar.png')
  plt.show()
```
![](https://github.com/davidkorea/bikeshare_project/blob/master/images/group_bar.png)

through ```fontproperties=get_chinese_font()```,and ```prop=get_chinese_font()``` to show chinese font.

plt.xticks and make the x-label normal 

![](https://github.com/davidkorea/bikeshare_project/blob/master/images/group_bar_2.png)

