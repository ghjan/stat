# -*- coding=utf-8 -*-
# 一元线性回归分析例子

from sklearn import linear_model
import pandas as pd

'''
利用Python进行一元线性回归分析
主要运用sklearn包中的linear_model.LinearRegression方法。

https://zhuanlan.zhihu.com/p/21456680
'''


# Function to get data
def get_data(file_name):
    data = pd.read_csv(file_name, encoding='utf-8')
    X = []
    Y = []
    for time, city in zip(data['year'], data['beijing']):
        X.append([float(time)])
        Y.append(float(city))
    return X, Y


# Function for linear model
def linear_model_main(X_parameters, Y_parameters, predict_value):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_  # 截距
    predictions['coefficient'] = regr.coef_  # 回归系数
    predictions['predicted_value'] = predict
    return predictions


def test_body():
    x = (171, 175, 159, 155, 152, 158, 154, 164, 168, 166, 159, 164)
    Y = (57, 64, 41, 38, 35, 44, 41, 51, 57, 49, 47, 46)
    X = [[item, ] for item in x]
    print(X)
    print(Y)
    predict_time = 180
    predict_data(X, Y, predict_time)


def predict_data(X, Y, predict_time):
    result = linear_model_main(X, Y, predict_time)
    print "Intercept value ", result['intercept']
    print "coefficient", result['coefficient']
    print "Predicted value: ", result['predicted_value']


def test_beijing():
    X, Y = get_data(U'../datasets/beijing.csv')
    print(X)
    print(Y)
    predict_time = 2014
    predict_data(X, Y, predict_time)


if __name__ == '__main__':
    test_beijing()
    test_body()
