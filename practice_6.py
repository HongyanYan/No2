#-*- coding: utf-8 -*-
import xlrd
from numpy.core.function_base import linspace 
#打开EXCEL文件 
excel = xlrd.open_workbook('data.xlsx')
#获取第一个sheet
sheet = excel.sheets()[0]
from  statistics import mean,stdev,variance #均值，标准差，方差
#分别求四组x,y值的平均值
x1=mean(sheet.col_values(0))
y1=mean(sheet.col_values(1))
x2=mean(sheet.col_values(2))
y2=mean(sheet.col_values(3))
x3=mean(sheet.col_values(4))
y3=mean(sheet.col_values(5))
x4=mean(sheet.col_values(6))
y4=mean(sheet.col_values(7))
print('平均值：','x1=',x1,'y1=',y1,'x2=',x2,'y2=',y2,'x3=',x3,'y3=',y3,'x4=',x4,'y4=',y4)
#分别求四组x,y值的标准差
sx1=stdev(sheet.col_values(0))
sy1=stdev(sheet.col_values(1))
sx2=stdev(sheet.col_values(2))
sy2=stdev(sheet.col_values(3))
sx3=stdev(sheet.col_values(4))
sy3=stdev(sheet.col_values(5))
sx4=stdev(sheet.col_values(6))
sy4=stdev(sheet.col_values(7))
print('标准差：','sx1=',sx1,'sy1=',sy1,'sx2=',sx2,'sy2=',sy2,'sx3=',sx3,'sy3=',sy3,'sx4=',sx4,'sy4=',sy4)
#分别求四组x,y值的方差
vx1=variance(sheet.col_values(0))
vy1=variance(sheet.col_values(1))
vx2=variance(sheet.col_values(2))
vy2=variance(sheet.col_values(3))
vx3=variance(sheet.col_values(4))
vy3=variance(sheet.col_values(5))
vx4=variance(sheet.col_values(6))
vy4=variance(sheet.col_values(7))
print('方差：','vx1=',vx1,'vy1=',vy1,'vx2=',vx2,'vy2=',vy2,'vx3=',vx3,'vy3=',vy3,'vx4=',vx4,'vy4=',vy4)
import math
#分别求四组数据的皮尔逊相关系数，以pearson_r表示皮尔逊相关系数
def pearson_r(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = mean(x)
    avg_y = mean(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)
r1=pearson_r(sheet.col_values(0),sheet.col_values(1))
r2=pearson_r(sheet.col_values(2),sheet.col_values(3))
r3=pearson_r(sheet.col_values(4),sheet.col_values(5))
r4=pearson_r(sheet.col_values(6),sheet.col_values(7))
print('相关系数：','r1=',r1,'r2=',r2,'r3=',r3,'r4=',r4)

import pylab as np
np.figure(1) #创建图1
np.title('figure1')
np.xlabel('x')
np.ylabel('y')
np.plot(sheet.col_values(0), sheet.col_values(1),'*') #作散点图 1
#线性拟合
x = np.array(sheet.col_values(0))
y = np.array(sheet.col_values(1))
a,b = np.polyfit(x, y, 1)
predicted_y = a*np.array(x) + b
np.plot(x, predicted_y) #添加拟合直线

np.figure(2) #创建图 2
np.title('figure2')
np.xlabel('x')
np.ylabel('y')
np.plot(sheet.col_values(2), sheet.col_values(3),'*')#线性拟合
x = np.array(sheet.col_values(2))
y = np.array(sheet.col_values(3))
a,b = np.polyfit(x, y, 1)
predicted_y = a*np.array(x) + b
np.plot(x, predicted_y) #添加拟合直线

np.figure(3) #创建图 2
np.title('figure3')
np.xlabel('x')
np.ylabel('y')
np.plot(sheet.col_values(4), sheet.col_values(5),'*')#线性拟合
x = np.array(sheet.col_values(4))
y = np.array(sheet.col_values(5))
a,b = np.polyfit(x, y, 1)
predicted_y = a*np.array(x) + b
np.plot(x, predicted_y) #添加拟合直线

np.figure(4) #创建图 2
np.title('figure4')
np.xlabel('x')
np.ylabel('y')
np.plot(sheet.col_values(6), sheet.col_values(7),'*')#线性拟合
x = np.array(sheet.col_values(6))
y = np.array(sheet.col_values(7))
a,b = np.polyfit(x, y, 1)
predicted_y = a*np.array(x) + b
np.plot(x, predicted_y) #添加拟合直线

np.show() #将以上四张图像显示出来