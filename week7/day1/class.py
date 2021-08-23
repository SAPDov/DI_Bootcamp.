import numpy as np
import pandas as pd
lst = [2, 4, 6, 8, 13, 2020]
numpy_arr = np.array(lst)
print(numpy_arr)
# array([   2,    4,    6,    8,   13, 2020])

lst_2d = [[3, 5, 7, -4, 1], [0, 5, 33, -750, 2]]
numpy_arr1 = np.array(lst_2d)
print(numpy_arr1)
print(numpy_arr1[:, 1])
print(np.mean(numpy_arr))
print(numpy_arr + 5)

 # a = np.arange(9).reshape((3,3))
 # print(a)

 df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
