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
import matplotlib.pyplot as plt

import seaborn as sns  # 要注意的是一旦导入了seaborn，matplotlib的默认作图风格就会被覆盖成seaborn的格式


def draw_dist():
    births = pd.read_csv('../datasets/beijing.csv')
    # 对上表的prglngth列做一个直方图

    # % matplotlib inline  # 为了在jupyter notebook里作图，需要用到这个命令

    sns.distplot(births['prglngth'])

    sns.plt.show()
