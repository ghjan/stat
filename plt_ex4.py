# -*- coding: utf-8 -*-
from __future__ import division
# import matplotlib.pyplot as plt  
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties  
from pandas import Series, DataFrame

def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


def draw_a_bar(index, y):
    data = Series(y, index=list(index))
    my_colors = 'rgbkymc'
    data.plot(kind='bar', alpha=0.7, color=my_colors)   
    plt.show()  
def draw_a_pie(labels,values):

    explode = [0.1 for i in labels]
    # from pylab import *  
    # mpl.rcParams['font.sans-serif'] = ['SimHei']  
    plt.pie(values, explode=explode, labels=labels,
        autopct='%1.1f%%', startangle=67)
    plt.show() 

def test_2():
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  
      
    plt.xlabel(u"电压差(V)", fontproperties=font)  
    plt.ylabel(u"介质损耗角差(度)", fontproperties=font)  
    plt.title(u"介质损耗角和荷电状态SOC关系图",fontproperties=font)     

if __name__=='__main__':
    set_ch()      
    # test_2()
    # plt.title(u'显示中文')
    # plt.show()    
    label='食品 服装 出行 教育 医疗 其他'
    consume='2500,1000,500,800,400,600'
    labels=  [_.decode("UTF-8") for _ in label.split(' ')]
    # labels= [u'食品',u'服装',u'出行',u'教育',u'医疗',u'其他']
    values = [int(_) for _ in consume.split(',')]
    draw_a_bar(labels, values)
    draw_a_pie(labels, values)    

    