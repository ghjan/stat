# -*- coding=utf-8 -*-
# 多元线性回归分析例子
'''
多元线性回归分析例子
参考
 Python实现机器学习二（实现多元线性回归）
http://blog.csdn.net/lulei1217/article/details/49386295

'''
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns  # 要注意的是一旦导入了seaborn，matplotlib的默认作图风格就会被覆盖成seaborn的格式


def draw_dist(data):
    # 对上表的prglngth列做一个直方图

    # % matplotlib inline  # 为了在jupyter notebook里作图，需要用到这个命令

    # sns.pairplot(data, x_vars=['TV', 'radio', 'newspaper'], y_vars='sales', size=7, aspect=0.8)
    sns.pairplot(data, x_vars=['TV', 'radio', 'newspaper'], y_vars='sales', size=7, aspect=0.8, kind='reg')
    plt.show()  # 注意必须加上这一句，否则无法显示。


def training(data, feature_cols):
    # create a python list of feature names
    # use the list to select a subset of the original DataFrame
    X = data[feature_cols]
    # equivalent command to do this in one line
    # X = data[['TV', 'radio', 'newspaper']]
    # select a Series from the DataFrame
    # y = data['sales']
    # equivalent command that works if there are no spaces in the column name
    y = data.sales
    ##构造训练集和测试集
    from sklearn.cross_validation import train_test_split  # 这里是引用了交叉验证
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    print X_train.shape
    print y_train.shape
    print X_test.shape
    print y_test.shape
    return X_train, y_train


def line_regression(X_train, y_train, feature_cols):
    from sklearn.linear_model import LinearRegression
    linreg = LinearRegression()
    model = linreg.fit(X_train, y_train)
    print model
    print linreg.intercept_
    print linreg.coef_
    # pair the feature names with the coefficients
    print(zip(feature_cols, linreg.coef_))


if __name__ == '__main__':
    feature_cols = ['TV', 'radio', 'newspaper']
    data = pd.read_csv('../datasets/Advertising.csv')
    # draw_dist(data)
    X_train, y_train = training(data, feature_cols)
    line_regression(X_train, y_train, feature_cols)
