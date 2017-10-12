# -*- coding=utf-8 -*-
# 多元线性回归分析例子
'''
多元线性回归分析例子
参考
 Python实现机器学习二（实现多元线性回归）
http://blog.csdn.net/lulei1217/article/details/49386295

'''
from sklearn import linear_model
import pandas as pd

# Function to get data
def get_data(file_name):
    data = pd.read_csv(file_name, encoding='utf-8')
    X = []
    Y = []
    for time, city in zip(data['year'], data['beijing']):
        X.append([float(time)])
        Y.append(float(city))
    return X, Y

