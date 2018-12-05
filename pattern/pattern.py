# -*- coding: UTF-8 -*-

# Filename : dataTransfer.py
# author by : Jay

#!/usr/bin/env python3
import re

print(re.match('www', 'www.taobao.com').span())
print(re.match('cn', 'www.taobao.com'))

line = "Cats are smarter than dogs"

matchObject = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObject:
	print("matchObject.group():", matchObject.group())
	print("matchObject.group(1):", matchObject.group(1))
	print("matchObject.group(2):", matchObject.group(2))
else:
	print("No match!")
	
print(re.search('www', 'www.taobao.cn').span())
print(len('www.taobao.com'))
print(re.search('com', 'www.taobao.com').span())

searchObject = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObject:
	print("searchObject.group():", searchObject.group())
	print("searchObject.group(1):", searchObject.group(1))
	print("searchObject.group(2):", searchObject.group(2))
else:
	print("No match!")
	
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
#re.search匹配整个字符串，直到找到一个匹配。

#re.sub 替换字符串
phone = "2004-959-559 # 这是一个电话号码"

num = re.sub(r'#.*$', '', phone)
print("num is :" + num)

digtal = re.sub(r'\D', '', phone)
print("num is :" + digtal)