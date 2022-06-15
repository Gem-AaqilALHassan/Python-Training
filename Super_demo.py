# Python program to demonstrate
# super function


class Animals:
	
	# Initializing constructor
	def __init__(self):
		self.legs = 4
		self.domestic = True
		self.tail = True
		self.mammals = True
	
	def isMammal(self):
		if self.mammals:
			print("It is a mammal.")
	
	def isDomestic(self):
		if self.domestic:
			print("It is a domestic animal.")
	
class Dogs(Animals):
	def __init__(self):
		super().__init__()

	def isMammal(self):
		super().isMammal()

class Horses(Animals):
	def __init__(self):
		super().__init__()

	def hasTailandLegs(self):
		if self.tail and self.legs == 4:
			print("Has legs and tail")

# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()


# Super function in multiple inheritance 

class Mammal():
	
	def __init__(self, name):
		print(name, "Is a mammal")
		
class canFly(Mammal):
	
	def __init__(self, canFly_name):
		print(canFly_name, "cannot fly")
		
		# Calling Parent class
		# Constructor
		super().__init__(canFly_name)
			
class canSwim(Mammal):
	
	def __init__(self, canSwim_name):
		
		print(canSwim_name, "cannot swim")
			
		super().__init__(canSwim_name)
		
class Animal(canFly, canSwim):
	
	def __init__(self, name):
		
		# Calling the constructor
		# of both the parent
		# class in the order of
		# their inheritance
		super().__init__(name)


# Driver Code
Carol = Animal("Dog")
