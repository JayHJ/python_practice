# -*- coding: UTF-8 -*-

# Filename : dataTransfer.py
# author by : Jay

#!/usr/bin/env python3

# 获取用户输入十进制数
dec = int(input("输入数字："))

print("十进制数为：", dec)
print("二进制数为：", bin(dec))
print("八进制数为：", oct(dec))
print("十六进制数为：", hex(dec))


#ASCII码与字符相互转换

# 用户输入字符
c = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))

print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))


#最小公倍数算法

def lcm(x, y):
	#获取最大数
	if (x > y):
		greater = x
	else:
		greater = y
		
	while(True):
		if ((greater % x == 0) and (greater % y == 0)):
			lcm = greater
			break
		greater +=1
		
	return greater

print(lcm(54, 24))