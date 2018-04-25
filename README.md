> repo정리하기 때문에 어제한 컨트리뷰션스 다 없어졌네ㅠㅠ

# bikeshare
Everage riding time for each quarter in 2017
 
# Issue 1 - .gitignore
 
If the size of a sigle file is bigger than 50M, could not be uoloaded to github.

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
* ```bool_arr```: through ```data_arr[;, -1] == type```, select only the last one column and return/change it to the boolean array. Also it it a one demention array,because we select only one(last) column.that why ```bool_arr.shape = (646586,)```
* when we process x[y], the mask array (bool_arr) will be expanded automatically as the same demention as the raw data(arrar x). another words, (646586, 9) + (646586, ) = (528509, 9)/filtered_arr 

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
