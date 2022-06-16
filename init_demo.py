# __init__

# A Sample class with init method
class Person:
	
	# init method or constructor
	def __init__(self, name):
		self.name = name
	
	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)
	
p = Person('Nikhil')
p.say_hi()

# __init__ with inheritance

# Python program to
# demonstrate init with
# inheritance

class A(object):
	def __init__(self, something):
		print("A init called")
		self.something = something
		

class B(A):
	def __init__(self, something):
		# Calling init of parent class
		A.__init__(self, something)
		print("B init called")
		self.something = something
		
obj = B("Something")
