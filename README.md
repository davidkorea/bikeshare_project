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

# Project Summary

### 01 mean duration

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

### 02 mean duration by user tupe
 
* Subject

  - filter data by boolean array
  - create a n-demention array ndarray
  - matplotlib
  
