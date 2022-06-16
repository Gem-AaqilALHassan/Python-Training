print("Enter the num1")
num1 = int(input())
print("Enter the num2")
num2 = int(input())
try:
    print("the sum of these two numbers is", num1+num2)
except exception as e:
	print(e)


# Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
	print ("Second element = %d" %(a[1]))

	# Throws error since there are only 3 elements in array
	print ("Fourth element = %d" %(a[3]))

except exception as e:
	print (e)


# Program to handle multiple errors with one
# except statement
# Python 3

def fun(a):
	if a < 4:

		# throws ZeroDivisionError for a = 3
		b = a/(a-3)

	# throws NameError if a >= 4
	print("Value of b = ", b)
	
try:
	fun(3)
	fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")
except exception as e:
	print(e)
