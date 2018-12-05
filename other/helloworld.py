# -*- coding: UTF-8 -*-
# Filename : helloworld.py
# author by : Jay

print('Hello world')


num1 = input('input first number:')
num2 = input('input second number:')

sum = float(num1) + float(num2)

print('sum of num {0} and num{1}: {2}'.format(num1, num2, sum))


# 平方根

num3 = input('input third number:')
num_sqt = float(num3) ** 0.5
print('{0} 的平方根为 {1}'.format(num3 ,num_sqt)) 

# 三角形面积
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

# 计算半周长
s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) **0.5
print('三角形面积为:{0}'.format(area))


#摄氏温度转华氏温度
# 用户输入摄氏温度

# 接收用户收入
celsius = float(input('输入摄氏温度: '))

# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' %(celsius,fahrenheit))