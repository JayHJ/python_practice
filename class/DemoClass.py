#!/usr/bin/python3

class DemoClass:
	i = 12345
	#class method, must have self as the first parameter
	def f(self):
		print("private access in method" + self.__privateVar)
		return 'hello world'
	# private var, can not be access outside of class
	__privateVar = 'test'
	
	def __privateMethod(self):
		print('this is private method, can only be access in the class but not outside of class')
		
	# only one __init__ function allowed
	# if multiple __init__ exist, last one will be used
	def __init__(self):
		self.data = []
		
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart
		print("private access in constructor" + self.__privateVar)



class people:
	#basic var
	name = ''
	age = 0
	#private var
	__weight = 0
	#constructor
	def __init__(self, n, a, w):
		self.name = n
		self.age = a
		self.__weight = w
	def speak(self):
		print('{0} speak : I am {1} years old'.format(self.name, self.age))
		
	def myMethod(self):
		print('this is parent method')


class student(people):
	grade = ''
	def __init__(self, n, a, w, g):
		people.__init__(self, n, a, w)
		self.grade = g
		
	def speak(self):
		print('{0} speak : I am {1} years old, and in {2} grade'.format(self.name, self.age, self.grade))
	
	#override the parent method
	def myMethod(self):
		print('this is child method')
		
p = people('Lucy',10, 10)
p.myMethod()
p.speak()
print("---------------")
z = student('Lucy', 10, 12, 3)
z.speak()
z.myMethod()

print("---------------")
x = DemoClass(11, 12)

print(x.f())
print(x.i)	

print("---------------")
y = DemoClass('test', 'ttt')
print(y.r)
print(y.i)
try:
	print(y.__privateVar)
except AttributeError as e:
	print("exception here" + str(e))
else:
	print("private var can not be access")