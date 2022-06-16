# Python3 program to
# demonstrate instantiating
# a class


class Dog:
	
	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

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



# Python3 program to show that we can create
# instance variables inside methods
	
# Class for Dog
class Dog:
	
	# Class Variable
	animal = 'dog'	
	
	# The init method or constructor
	def __init__(self, breed):
		
		# Instance Variable
		self.breed = breed			

	# Adds an instance variable
	def setColor(self, color):
		self.color = color
	
	# Retrieves instance variable	
	def getColor(self):	
		return self.color

# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
