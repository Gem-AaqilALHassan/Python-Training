# Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


# Single Inheritance:

# Python program to demonstrate error if we
# forget to invoke __init__() of the parent.

class A:
	def __init__(self, n = 'Rahul'):
			self.name = n
class B(A):
	def __init__(self, roll):
			self.roll = roll

object = B(23)
print (object.name)


# Multiple inheritance:

# Python example to show the working of multiple
# inheritance
class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")

class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"	
		print("Base2")

class Derived(Base1, Base2):
	def __init__(self):
		
		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")
		
	def printStrs(self):
		print(self.str1, self.str2)
		

ob = Derived()
ob.printStrs()

Multilevel inheritance: 

# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Base(object):
	
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):
	
	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get name
	def getAge(self):
		return self.age

# Inherited or Sub class (Note Person in bracket)
class GrandChild(Child):
	
	# Constructor
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address	

# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())


# Python program to demonstrate private members
# of the parent class
class C(object):
	def __init__(self):
			self.c = 21

			# d is private instance variable
			self.__d = 42
class D(C):
	def __init__(self):
			self.e = 84
			C.__init__(self)
object1 = D()

# produces an error as d is private instance variable
print(object1.d)					
